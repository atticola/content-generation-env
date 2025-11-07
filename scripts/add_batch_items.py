#!/usr/bin/env python3
"""
Add batch-generated items to drafts file
"""

import json
import sys

def add_batch_items():
    """Add multiple items from AI batch generation"""

    print("\n" + "=" * 70)
    print("  Add Batch Items to Drafts")
    print("=" * 70)

    # Get JSON array from user
    print("\nPaste the JSON array from AI (all 17 items).")
    print("Press Ctrl+D (Mac/Linux) or Ctrl+Z (Windows) when done:\n")

    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass

    json_text = '\n'.join(lines)

    # Parse the JSON array
    print("\n📊 Parsing JSON array...")
    try:
        items = json.loads(json_text)
    except json.JSONDecodeError as e:
        print(f"\n❌ Invalid JSON: {e}")
        print("\nMake sure you pasted a valid JSON array starting with [ and ending with ]")
        sys.exit(1)

    if not isinstance(items, list):
        print("\n❌ Expected a JSON array (starting with [)")
        sys.exit(1)

    print(f"✅ Parsed {len(items)} items")

    # Load drafts file
    print("\n📂 Loading drafts file...")
    try:
        with open('drafts/suggestion-EN.next.json', 'r', encoding='utf-8') as f:
            draft_data = json.load(f)
    except FileNotFoundError:
        print("❌ drafts/suggestion-EN.next.json not found!")
        sys.exit(1)

    # Quick validation of each item
    print("\n🔍 Quick validation...")
    errors = []
    warnings = []

    for idx, item in enumerate(items, start=2):
        item_num = f"Item #{idx}"

        # Check required fields
        required = ['id', 'header', 'contentShort', 'contentLong', 'keywords', 'label']
        missing = [f for f in required if f not in item]
        if missing:
            errors.append(f"{item_num}: Missing fields: {missing}")
            continue

        # Check header length
        header_len = len(item['header'])
        if not (48 <= header_len <= 80):
            warnings.append(f"{item_num}: Header length {header_len} (should be 48-80)")

        # Check content short
        if len(item['contentShort']) > 120:
            errors.append(f"{item_num}: Content short too long ({len(item['contentShort'])} chars)")

        # Check keywords
        keywords = item['keywords'].split(';')
        if not (6 <= len(keywords) <= 14):
            warnings.append(f"{item_num}: {len(keywords)} keywords (should be 6-14)")

        if item['keywords'].endswith(';'):
            errors.append(f"{item_num}: Keywords have trailing semicolon")

    if errors:
        print("\n❌ VALIDATION ERRORS:")
        for error in errors:
            print(f"   • {error}")
        print("\nFix these errors before adding items.")
        sys.exit(1)

    if warnings:
        print("\n⚠️  WARNINGS:")
        for warning in warnings:
            print(f"   • {warning}")
        print("\nContinuing anyway...")

    # Distribute items to appropriate groups
    print("\n📦 Adding items to groups...")

    group_mapping = {
        'heart_health': 'heart_health',
        'popular': 'popular'
    }

    items_added = {
        'heart_health': 0,
        'popular': 0
    }

    for idx, item in enumerate(items, start=2):
        # Determine which group based on label/topic
        # Items 2-4, 6-9, 12-18 → heart_health
        # Items 5, 10-11 → popular

        if idx in [5, 10, 11]:
            target_group = 'popular'
        else:
            target_group = 'heart_health'

        # Find the group and add item
        for group in draft_data['data']:
            if group['key'] == target_group:
                group['suggestionItem'].append(item)
                items_added[target_group] += 1
                print(f"   ✅ Item #{idx} → {target_group}")
                break

    # Save updated draft file
    print("\n💾 Saving to drafts/suggestion-EN.next.json...")
    with open('drafts/suggestion-EN.next.json', 'w', encoding='utf-8') as f:
        json.dump(draft_data, f, indent=2, ensure_ascii=False)

    # Summary
    print("\n" + "=" * 70)
    print("✅ SUCCESS!")
    print("=" * 70)
    print(f"\n📊 Added {len(items)} items:")
    for group, count in items_added.items():
        if count > 0:
            print(f"   • {group}: {count} items")

    print("\n🎯 NEXT STEPS:")
    print("   1. Run validation: python3 validate.py")
    print("   2. Review items: python3 edit_item.py")
    print("   3. Create Pull Request when ready")

    print("\n" + "=" * 70 + "\n")

if __name__ == "__main__":
    try:
        add_batch_items()
    except KeyboardInterrupt:
        print("\n\n❌ Cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

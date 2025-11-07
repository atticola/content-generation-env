#!/usr/bin/env python3
"""
Simple script to edit an existing suggestion item.
This script helps non-coders edit content items easily.
"""

import json
import sys
from datetime import datetime

def get_input(prompt, default=None):
    """Get user input with optional default value"""
    if default:
        user_input = input(f"{prompt}\n   Current: {default}\n   New (or press Enter to keep): ").strip()
        return user_input if user_input else default
    return input(f"{prompt}: ").strip()

def find_item_by_id(data, item_id):
    """Find an item by its ID across all groups"""
    for group in data['data']:
        for idx, item in enumerate(group['suggestionItem']):
            if item['id'] == item_id:
                return group, idx, item
    return None, None, None

def list_all_items(data):
    """List all items with their IDs and headers"""
    print("\n📋 Available Items:")
    print("-" * 80)
    item_count = 0
    for group in data['data']:
        if group['suggestionItem']:
            print(f"\n🗂️  Group: {group['name']} ({group['key']})")
            for item in group['suggestionItem']:
                item_count += 1
                status_emoji = "📝" if item['status'] == "DRAFT" else "✅" if item['status'] == "ACTIVE" else "🔄"
                print(f"   {status_emoji} {item['id'][:8]}... - {item['header'][:50]}")
                print(f"      Status: {item['status']}, Rev: {item['revision']}")
    print(f"\n📊 Total items: {item_count}")
    print("-" * 80)

def edit_suggestion_item():
    """Interactive function to edit an existing suggestion item"""
    print("\n" + "="*60)
    print("  Welcome to Suggestion Item Editor!")
    print("="*60)
    print("\nI'll help you edit an existing health content item.\n")

    # Load draft file
    try:
        with open('drafts/suggestion-EN.next.json', 'r', encoding='utf-8') as f:
            draft_data = json.load(f)
    except FileNotFoundError:
        print("❌ Error: drafts/suggestion-EN.next.json not found!")
        sys.exit(1)

    # List all items
    list_all_items(draft_data)

    # Get item ID
    print("\n🔍 FIND ITEM")
    print("-" * 60)
    item_id = input("\nEnter the item ID (full or first 8 characters): ").strip()

    # Find the item (support partial ID match)
    group, idx, item = None, None, None
    for g in draft_data['data']:
        for i, itm in enumerate(g['suggestionItem']):
            if itm['id'].startswith(item_id):
                group, idx, item = g, i, itm
                break
        if item:
            break

    if not item:
        print(f"❌ Error: Item with ID '{item_id}' not found!")
        sys.exit(1)

    print(f"\n✅ Found item: {item['header']}")
    print(f"   ID: {item['id']}")
    print(f"   Status: {item['status']}")
    print(f"   Revision: {item['revision']}")

    # Edit options
    print("\n\n✏️  EDIT OPTIONS")
    print("-" * 60)
    print("\nWhat would you like to edit?")
    print("1. Header (title)")
    print("2. Content Short (teaser)")
    print("3. Content Long (main content)")
    print("4. Keywords")
    print("5. Label (category)")
    print("6. Image Path")
    print("7. Status")
    print("8. View current content")
    print("9. Done (save changes)")

    changes_made = False

    while True:
        choice = input("\nEnter option number (1-9): ").strip()

        if choice == "1":
            new_header = get_input("\n📝 Edit Header (48-80 chars)", item['header'])
            if new_header != item['header']:
                item['header'] = new_header
                changes_made = True
                print("✅ Header updated")

        elif choice == "2":
            new_short = get_input("\n📝 Edit Content Short (max 120 chars)", item['contentShort'])
            if new_short != item['contentShort']:
                item['contentShort'] = new_short
                changes_made = True
                print("✅ Content Short updated")

        elif choice == "3":
            print("\n📝 Edit Content Long")
            print("Current content:")
            print("-" * 60)
            print(item['contentLong'][:200] + "..." if len(item['contentLong']) > 200 else item['contentLong'])
            print("-" * 60)
            print("\nEnter new content (press Enter twice when done):")

            content_lines = []
            empty_count = 0
            while empty_count < 2:
                line = input()
                if line.strip() == "":
                    empty_count += 1
                else:
                    empty_count = 0
                    content_lines.append(line)

            new_long = "\n".join(content_lines).strip()
            if new_long and new_long != item['contentLong']:
                item['contentLong'] = new_long
                changes_made = True
                print("✅ Content Long updated")

        elif choice == "4":
            new_keywords = get_input("\n📝 Edit Keywords (semicolon-separated)", item['keywords'])
            if new_keywords != item['keywords']:
                item['keywords'] = new_keywords
                changes_made = True
                print("✅ Keywords updated")

        elif choice == "5":
            new_label = get_input("\n📝 Edit Label", item['label'])
            if new_label != item['label']:
                item['label'] = new_label
                changes_made = True
                print("✅ Label updated")

        elif choice == "6":
            new_image = get_input("\n📝 Edit Image Path (must be https://)", item['imagePath'])
            if new_image != item['imagePath']:
                item['imagePath'] = new_image
                changes_made = True
                print("✅ Image Path updated")

        elif choice == "7":
            print("\n📝 Edit Status")
            print("Current status:", item['status'])
            print("\nOptions:")
            print("  DRAFT - Still being created")
            print("  IN_REVIEW - Sent for review")
            print("  CHANGES_REQUESTED - Needs changes")
            print("  APPROVED - Approved by reviewers")
            print("  ACTIVE - Published and live")
            print("  INACTIVE - Archived")

            new_status = input("\nNew status: ").strip().upper()
            if new_status in ["DRAFT", "IN_REVIEW", "CHANGES_REQUESTED", "APPROVED", "ACTIVE", "INACTIVE"]:
                if new_status != item['status']:
                    item['status'] = new_status
                    reason = input("Status reason (e.g., REVIEW_CHANGES, APPROVED_FOR_PUBLISH): ").strip()
                    item['statusReason'] = reason if reason else "STATUS_UPDATED"
                    changes_made = True
                    print("✅ Status updated")
            else:
                print("❌ Invalid status")

        elif choice == "8":
            print("\n" + "="*60)
            print("CURRENT ITEM CONTENT")
            print("="*60)
            print(json.dumps(item, indent=2, ensure_ascii=False))
            print("="*60)

        elif choice == "9":
            break

        else:
            print("❌ Invalid option. Please choose 1-9.")

    if not changes_made:
        print("\n⚠️  No changes made. Exiting without saving.")
        return

    # Update metadata
    item['revision'] += 1
    item['updatedDate'] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    item['updatedBy'] = "content-editor"

    # Save changes
    print("\n\n💾 SAVING CHANGES...")
    print("-" * 60)

    with open('drafts/suggestion-EN.next.json', 'w', encoding='utf-8') as f:
        json.dump(draft_data, f, indent=2, ensure_ascii=False)

    print("\n✅ SUCCESS!")
    print("="*60)
    print(f"\n📄 Item updated: {item['id']}")
    print(f"📝 New revision: {item['revision']}")
    print(f"📁 Status: {item['status']}")
    print(f"\n📂 File updated:")
    print(f"   - drafts/suggestion-EN.next.json")
    print("\n🎯 NEXT STEPS:")
    print("   1. Review your changes in drafts/suggestion-EN.next.json")
    print("   2. Update or create a Pull Request when ready")
    print("   3. Tag appropriate reviewers if needed")
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    try:
        edit_suggestion_item()
    except KeyboardInterrupt:
        print("\n\n❌ Cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

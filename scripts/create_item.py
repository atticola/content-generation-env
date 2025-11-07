#!/usr/bin/env python3
"""
Simple script to create a new suggestion item.
This script helps non-coders create content items easily.
"""

import json
import uuid
from datetime import datetime
import sys

def get_input(prompt, default=None):
    """Get user input with optional default value"""
    if default:
        user_input = input(f"{prompt} (default: {default}): ").strip()
        return user_input if user_input else default
    return input(f"{prompt}: ").strip()

def create_suggestion_item():
    """Interactive function to create a new suggestion item"""
    print("\n" + "="*60)
    print("  Welcome to Suggestion Item Creator!")
    print("="*60)
    print("\nI'll guide you through creating a new health content item.")
    print("Just answer the questions below.\n")

    # Get basic information
    print("📋 BASIC INFORMATION")
    print("-" * 60)

    group_key = get_input("\n1. Which group should this go in?\n   Options: latest_read, popular, heart_health", "latest_read")
    label = get_input("\n2. What category is this?\n   Examples: cardiology, lipids, prevention, lifestyle", "cardiology")

    print("\n\n📝 CONTENT")
    print("-" * 60)

    header = get_input("\n3. Write a compelling title (48-80 characters)\n   You can include ONE emoji if you like",
                       "Understanding Your Heart Health ❤️")

    content_short = get_input("\n4. Write a short teaser (max 120 characters)\n   This appears in preview cards",
                              "Learn about heart health and how to protect it.")

    print("\n5. Now for the main content (HTML format)")
    print("   Use these tags: <p>, <ul>, <ol>, <li>, <b>, <i>, <br>")
    print("   Example template:")
    print("   <p><b>Headline</b></p>")
    print("   <p>Introduction text here.</p>")
    print("   <ul><li>Point 1</li><li>Point 2</li></ul>")
    print("\n   Type or paste your content (press Enter twice when done):")

    content_lines = []
    empty_count = 0
    while empty_count < 2:
        line = input()
        if line.strip() == "":
            empty_count += 1
        else:
            empty_count = 0
            content_lines.append(line)

    content_long = "\n".join(content_lines).strip()

    if not content_long:
        content_long = "<p><b>Sample Content</b></p><p>This is a placeholder. Please edit this content.</p>"

    keywords = get_input("\n6. Enter keywords (6-14 words, separated by semicolons)\n   Mix Turkish and English for better search\n   Example: LDL;kolesterol;cholesterol;kalp;heart",
                        "heart;kalp;health;sağlık;cardiology;kardiyoloji")

    image_path = get_input("\n7. Image URL (must start with https://)",
                          "https://example.com/images/health_default.png")

    # Generate metadata
    item_id = str(uuid.uuid4())
    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    # Create the item
    item = {
        "id": item_id,
        "revision": 1,
        "createdDate": now,
        "updatedDate": now,
        "createdBy": "content-creator",
        "updatedBy": "content-creator",
        "status": "DRAFT",
        "statusReason": "CREATED",
        "index": 999,
        "keywords": keywords,
        "label": label,
        "header": header,
        "contentShort": content_short,
        "contentLong": content_long,
        "imagePath": image_path,
        "readingFeatureEnabled": False,
        "parameter": [],
        "readCount": 0,
        "likedCount": 0,
        "bookmarkedCount": 0
    }

    # Create review stub
    review_stub = {
        "medical": [],
        "product": [],
        "context": []
    }

    # Save to files
    print("\n\n💾 SAVING...")
    print("-" * 60)

    # Load existing draft file
    try:
        with open('drafts/suggestion-EN.next.json', 'r', encoding='utf-8') as f:
            draft_data = json.load(f)
    except FileNotFoundError:
        print("❌ Error: drafts/suggestion-EN.next.json not found!")
        sys.exit(1)

    # Find the target group and add the item
    found_group = False
    for group in draft_data['data']:
        if group['key'] == group_key:
            group['suggestionItem'].append(item)
            found_group = True
            break

    if not found_group:
        print(f"❌ Error: Group '{group_key}' not found!")
        sys.exit(1)

    # Save updated draft file
    with open('drafts/suggestion-EN.next.json', 'w', encoding='utf-8') as f:
        json.dump(draft_data, f, indent=2, ensure_ascii=False)

    # Save review stub
    with open(f'reviews/{item_id}.review.json', 'w', encoding='utf-8') as f:
        json.dump(review_stub, f, indent=2, ensure_ascii=False)

    # Save item JSON for reference
    with open(f'reviews/{item_id}.item.json', 'w', encoding='utf-8') as f:
        json.dump(item, f, indent=2, ensure_ascii=False)

    print("\n✅ SUCCESS!")
    print("="*60)
    print(f"\n📄 Item created with ID: {item_id}")
    print(f"📁 Added to group: {group_key}")
    print(f"📝 Status: DRAFT")
    print(f"\n📂 Files created:")
    print(f"   - drafts/suggestion-EN.next.json (updated)")
    print(f"   - reviews/{item_id}.review.json (review stub)")
    print(f"   - reviews/{item_id}.item.json (item copy)")
    print("\n🎯 NEXT STEPS:")
    print("   1. Review your content in drafts/suggestion-EN.next.json")
    print("   2. Create a Pull Request when ready for review")
    print("   3. Tag appropriate reviewers (medical, product, content)")
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    try:
        create_suggestion_item()
    except KeyboardInterrupt:
        print("\n\n❌ Cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        sys.exit(1)

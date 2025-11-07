#!/usr/bin/env python3
"""
Simple validation script to check suggestion items.
This helps ensure content follows all the rules.
"""

import json
import re
import sys
from datetime import datetime

def validate_uuid(uuid_string):
    """Validate UUID v4 format"""
    pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    return bool(re.match(pattern, uuid_string.lower()))

def validate_date(date_string):
    """Validate ISO 8601 date format"""
    try:
        datetime.strptime(date_string.replace('Z', '+0000'), '%Y-%m-%dT%H:%M:%S.%f%z')
        return True
    except:
        return False

def validate_html(html):
    """Check for forbidden HTML tags"""
    forbidden = ['<script', '<style', '<iframe', '<object', '<a']
    for tag in forbidden:
        if tag in html.lower():
            return False, f"Forbidden tag found: {tag}"
    return True, "OK"

def validate_keywords(keywords):
    """Validate keywords format"""
    if keywords.endswith(';'):
        return False, "Keywords should not end with semicolon"

    tokens = [k.strip() for k in keywords.split(';') if k.strip()]
    if len(tokens) < 6:
        return False, f"Too few keywords ({len(tokens)}). Need at least 6."
    if len(tokens) > 14:
        return False, f"Too many keywords ({len(tokens)}). Maximum is 14."

    return True, f"{len(tokens)} keywords"

def validate_item(item, group_key):
    """Validate a single suggestion item"""
    errors = []
    warnings = []

    # Required fields
    required = ['id', 'revision', 'createdDate', 'updatedDate', 'createdBy', 'updatedBy',
                'status', 'statusReason', 'index', 'keywords', 'label', 'header',
                'contentShort', 'contentLong', 'imagePath', 'readingFeatureEnabled',
                'parameter', 'readCount', 'likedCount', 'bookmarkedCount']

    for field in required:
        if field not in item:
            errors.append(f"Missing required field: {field}")

    if errors:
        return errors, warnings  # Stop here if critical fields missing

    # Validate UUID
    if not validate_uuid(item['id']):
        errors.append(f"Invalid UUID format: {item['id']}")

    # Validate revision
    if not isinstance(item['revision'], int) or item['revision'] < 1:
        errors.append(f"Invalid revision: {item['revision']} (must be integer ≥ 1)")

    # Validate dates
    if not validate_date(item['createdDate']):
        errors.append(f"Invalid createdDate format: {item['createdDate']}")
    if not validate_date(item['updatedDate']):
        errors.append(f"Invalid updatedDate format: {item['updatedDate']}")

    # Validate status
    valid_statuses = ['DRAFT', 'IN_REVIEW', 'CHANGES_REQUESTED', 'APPROVED', 'ACTIVE', 'INACTIVE']
    if item['status'] not in valid_statuses:
        errors.append(f"Invalid status: {item['status']}")

    # Validate header length
    header_len = len(item['header'])
    if header_len < 48:
        warnings.append(f"Header too short ({header_len} chars). Minimum is 48.")
    elif header_len > 80:
        errors.append(f"Header too long ({header_len} chars). Maximum is 80.")

    # Validate contentShort
    short_len = len(item['contentShort'])
    if short_len > 120:
        errors.append(f"Content short too long ({short_len} chars). Maximum is 120.")

    if '<' in item['contentShort']:
        errors.append("Content short should not contain HTML tags")

    # Validate contentLong HTML
    html_valid, html_msg = validate_html(item['contentLong'])
    if not html_valid:
        errors.append(f"Content long: {html_msg}")

    # Validate keywords
    kw_valid, kw_msg = validate_keywords(item['keywords'])
    if not kw_valid:
        errors.append(f"Keywords: {kw_msg}")
    else:
        warnings.append(f"Keywords: {kw_msg}")

    # Validate imagePath
    if not item['imagePath'].startswith('https://'):
        errors.append(f"Image path must be HTTPS URL: {item['imagePath']}")

    # Validate metrics
    for metric in ['readCount', 'likedCount', 'bookmarkedCount']:
        if not isinstance(item[metric], int) or item[metric] < 0:
            errors.append(f"Invalid {metric}: {item[metric]} (must be integer ≥ 0)")

    # Validate index
    if not isinstance(item['index'], int) or item['index'] < 0:
        errors.append(f"Invalid index: {item['index']} (must be integer ≥ 0)")

    return errors, warnings

def validate_file(file_path):
    """Validate a suggestion JSON file"""
    print(f"\n🔍 Validating: {file_path}")
    print("=" * 80)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return False

    # Validate root structure
    if 'data' not in data:
        print("❌ Missing 'data' field in root")
        return False

    total_errors = 0
    total_warnings = 0
    total_items = 0

    # Validate each group
    for group_idx, group in enumerate(data['data']):
        print(f"\n📁 Group {group_idx + 1}: {group.get('name', 'Unknown')} ({group.get('key', 'Unknown')})")
        print("-" * 80)

        # Validate group structure
        if 'status' not in group or group['status'] not in ['ACTIVE', 'INACTIVE']:
            print(f"  ⚠️  Invalid group status: {group.get('status', 'Missing')}")
            total_warnings += 1

        # Validate items in group
        for item_idx, item in enumerate(group.get('suggestionItem', [])):
            total_items += 1
            errors, warnings = validate_item(item, group['key'])

            if errors or warnings:
                header = item.get('header', 'Unknown')[:50]
                item_id = item.get('id', 'Unknown')[:12]
                print(f"\n  📄 Item {item_idx + 1}: {header}...")
                print(f"     ID: {item_id}...")

                if errors:
                    total_errors += len(errors)
                    print(f"     ❌ Errors ({len(errors)}):")
                    for error in errors:
                        print(f"        • {error}")

                if warnings:
                    total_warnings += len(warnings)
                    print(f"     ⚠️  Warnings ({len(warnings)}):")
                    for warning in warnings:
                        print(f"        • {warning}")

    # Summary
    print("\n" + "=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)
    print(f"📊 Total items validated: {total_items}")
    print(f"❌ Total errors: {total_errors}")
    print(f"⚠️  Total warnings: {total_warnings}")

    if total_errors == 0:
        print("\n✅ Validation passed! No errors found.")
        if total_warnings > 0:
            print(f"⚠️  But there are {total_warnings} warnings to review.")
        return True
    else:
        print(f"\n❌ Validation failed with {total_errors} errors.")
        return False

def main():
    """Main validation function"""
    print("\n" + "=" * 80)
    print("  Suggestion Item Validator")
    print("=" * 80)

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        success = validate_file(file_path)
    else:
        # Validate both standard files
        print("\nValidating all standard files...\n")

        success1 = validate_file('data/suggestion-EN.json')
        success2 = validate_file('drafts/suggestion-EN.next.json')

        success = success1 and success2

    print("\n" + "=" * 80 + "\n")

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

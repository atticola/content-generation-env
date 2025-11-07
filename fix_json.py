#!/usr/bin/env python3
"""
Fix common JSON issues in suggestion files
Removes control characters and fixes formatting
"""

import json
import sys
import re

def clean_string(text):
    """Remove control characters except newlines and tabs"""
    if not isinstance(text, str):
        return text

    # Remove control characters except \n and \t
    cleaned = ''.join(char for char in text if ord(char) >= 32 or char in '\n\t')
    return cleaned

def clean_item(item):
    """Clean all string fields in an item"""
    if isinstance(item, dict):
        return {key: clean_item(value) for key, value in item.items()}
    elif isinstance(item, list):
        return [clean_item(element) for element in item]
    elif isinstance(item, str):
        return clean_string(item)
    else:
        return item

def fix_json_file(file_path):
    """Read, clean, and rewrite a JSON file"""
    print(f"\n🔧 Fixing: {file_path}")
    print("-" * 60)

    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        print(f"📊 Original size: {len(content)} bytes")

        # Try to parse it
        try:
            data = json.loads(content)
            print("✅ File is already valid JSON")
            return True

        except json.JSONDecodeError as e:
            print(f"⚠️  JSON Error found at position {e.pos}")
            print(f"   Line {e.lineno}, Column {e.colno}")
            print(f"   Error: {e.msg}")

            # Try to clean and re-parse
            print("\n🧹 Attempting to clean...")

            # Remove all control characters except newlines
            cleaned_content = ''.join(
                char for char in content
                if ord(char) >= 32 or char in '\n\t'
            )

            try:
                data = json.loads(cleaned_content)
                print("✅ Successfully cleaned and parsed!")

            except json.JSONDecodeError as e2:
                print(f"❌ Still has errors: {e2}")
                return False

        # Clean the data structure
        cleaned_data = clean_item(data)

        # Create backup
        backup_path = file_path + '.backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"💾 Backup saved: {backup_path}")

        # Write cleaned version
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(cleaned_data, f, indent=2, ensure_ascii=False)

        # Check new size
        with open(file_path, 'r', encoding='utf-8') as f:
            new_content = f.read()

        print(f"📊 New size: {len(new_content)} bytes")
        print("✅ File fixed and saved!")

        return True

    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return False

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def main():
    """Main function"""
    print("\n" + "=" * 60)
    print("  JSON File Fixer")
    print("=" * 60)

    if len(sys.argv) > 1:
        # Fix specific file
        file_path = sys.argv[1]
        success = fix_json_file(file_path)
    else:
        # Fix all standard files
        files = [
            'data/suggestion-EN.json',
            'drafts/suggestion-EN.next.json'
        ]

        success = all(fix_json_file(f) for f in files)

    print("\n" + "=" * 60)

    if success:
        print("✅ All files processed successfully!")
        print("\nYou can now run: python3 validate.py")
    else:
        print("❌ Some files had errors")
        print("\nCheck the error messages above")

    print("=" * 60 + "\n")

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

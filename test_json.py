#!/usr/bin/env python3
"""
Quick test to check all JSON files for syntax errors
"""

import json
import sys

files_to_test = [
    'data/suggestion-EN.json',
    'drafts/suggestion-EN.next.json',
    'schemas/suggestion.schema.json'
]

print("Testing JSON files for syntax errors...\n")

all_valid = True

for file_path in files_to_test:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"📄 {file_path}")
            print(f"   Size: {len(content)} bytes")

            data = json.loads(content)
            print(f"   ✅ Valid JSON\n")

    except json.JSONDecodeError as e:
        print(f"   ❌ JSON Error: {e}")
        print(f"   Position: {e.pos}")
        print(f"   Line: {e.lineno}, Column: {e.colno}\n")
        all_valid = False

    except FileNotFoundError:
        print(f"   ⚠️  File not found\n")
        all_valid = False

    except Exception as e:
        print(f"   ❌ Error: {e}\n")
        all_valid = False

if all_valid:
    print("✅ All JSON files are valid!")
    sys.exit(0)
else:
    print("❌ Some files have errors")
    sys.exit(1)

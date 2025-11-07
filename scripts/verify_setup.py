#!/usr/bin/env python3
"""
Verify that the complete environment is set up correctly
"""

import os
import json
import sys

def check_exists(path, item_type="file"):
    """Check if a path exists"""
    exists = os.path.exists(path)
    if item_type == "file":
        exists = exists and os.path.isfile(path)
    elif item_type == "dir":
        exists = exists and os.path.isdir(path)
    return exists

def verify_environment():
    """Verify all components of the environment"""
    print("\n" + "=" * 70)
    print("  ENVIRONMENT SETUP VERIFICATION")
    print("=" * 70)

    all_good = True
    errors = []
    warnings = []

    # Check folders
    print("\n📁 FOLDER STRUCTURE")
    print("-" * 70)
    folders = {
        'data': 'Published content',
        'drafts': 'Work in progress',
        'reviews': 'Review feedback',
        'schemas': 'Validation rules',
        'agent': 'AI agent instructions',
        'agent/prompts': 'Prompt templates',
        '.github': 'GitHub integration',
        '.github/workflows': 'CI/CD workflows',
        '.github/ISSUE_TEMPLATE': 'Issue templates'
    }

    for folder, description in folders.items():
        if check_exists(folder, "dir"):
            print(f"  ✅ {folder:<30} {description}")
        else:
            print(f"  ❌ {folder:<30} MISSING!")
            errors.append(f"Missing folder: {folder}")
            all_good = False

    # Check data files
    print("\n📄 DATA FILES")
    print("-" * 70)
    data_files = {
        'data/suggestion-EN.json': 'Production data',
        'drafts/suggestion-EN.next.json': 'Draft data',
        'schemas/suggestion.schema.json': 'JSON Schema'
    }

    for file_path, description in data_files.items():
        if check_exists(file_path):
            # Try to parse JSON
            try:
                with open(file_path, 'r') as f:
                    json.load(f)
                print(f"  ✅ {file_path:<35} {description} (valid JSON)")
            except json.JSONDecodeError as e:
                print(f"  ⚠️  {file_path:<35} Invalid JSON!")
                warnings.append(f"Invalid JSON: {file_path}")
        else:
            print(f"  ❌ {file_path:<35} MISSING!")
            errors.append(f"Missing file: {file_path}")
            all_good = False

    # Check agent files
    print("\n📄 AGENT FILES")
    print("-" * 70)
    agent_files = {
        'agent/agent.md': 'System specification',
        'agent/prompts/create_item.prompt.md': 'Creation prompt',
        'agent/prompts/edit_item.prompt.md': 'Editing prompt'
    }

    for file_path, description in agent_files.items():
        if check_exists(file_path):
            print(f"  ✅ {file_path:<40} {description}")
        else:
            print(f"  ❌ {file_path:<40} MISSING!")
            errors.append(f"Missing file: {file_path}")
            all_good = False

    # Check GitHub files
    print("\n📄 GITHUB FILES")
    print("-" * 70)
    github_files = {
        '.github/CODEOWNERS': 'Code owners',
        '.github/pull_request_template.md': 'PR template',
        '.github/workflows/validate.yml': 'CI validation',
        '.github/ISSUE_TEMPLATE/content_request.md': 'Content request template',
        '.github/ISSUE_TEMPLATE/edit_request.md': 'Edit request template'
    }

    for file_path, description in github_files.items():
        if check_exists(file_path):
            print(f"  ✅ {file_path:<45} {description}")
        else:
            print(f"  ❌ {file_path:<45} MISSING!")
            errors.append(f"Missing file: {file_path}")
            all_good = False

    # Check Python scripts
    print("\n🐍 PYTHON SCRIPTS")
    print("-" * 70)
    scripts = {
        'create_item.py': 'Create new items',
        'edit_item.py': 'Edit existing items',
        'validate.py': 'Validate content',
        'fix_json.py': 'Fix JSON issues',
        'test_json.py': 'Test JSON validity'
    }

    for script, description in scripts.items():
        if check_exists(script):
            # Check if executable
            is_executable = os.access(script, os.X_OK)
            status = "✅" if is_executable else "⚠️ "
            note = "" if is_executable else "(not executable)"
            print(f"  {status} {script:<25} {description} {note}")
            if not is_executable:
                warnings.append(f"Script not executable: {script}")
        else:
            print(f"  ❌ {script:<25} MISSING!")
            errors.append(f"Missing script: {script}")
            all_good = False

    # Check documentation
    print("\n📖 DOCUMENTATION")
    print("-" * 70)
    docs = {
        'README.md': 'Complete user guide',
        'QUICK_START.md': '5-minute guide',
        'PROJECT_OVERVIEW.md': 'Project overview'
    }

    for doc, description in docs.items():
        if check_exists(doc):
            # Check file size
            size = os.path.getsize(doc)
            print(f"  ✅ {doc:<30} {description} ({size:,} bytes)")
        else:
            print(f"  ❌ {doc:<30} MISSING!")
            errors.append(f"Missing documentation: {doc}")
            all_good = False

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    if errors:
        print(f"\n❌ ERRORS ({len(errors)}):")
        for error in errors:
            print(f"   • {error}")

    if warnings:
        print(f"\n⚠️  WARNINGS ({len(warnings)}):")
        for warning in warnings:
            print(f"   • {warning}")

        print("\n💡 To fix script permissions, run:")
        print("   chmod +x *.py")

    if all_good and not warnings:
        print("\n✅ PERFECT! All components are in place and working!")
        print("\n🎉 Your environment is ready to use!")
        print("\n🚀 NEXT STEPS:")
        print("   1. Read QUICK_START.md to get started")
        print("   2. Try creating your first item: python3 create_item.py")
        print("   3. Check the README.md for detailed documentation")

    elif all_good and warnings:
        print("\n✅ Environment is set up correctly!")
        print("⚠️  But there are some minor warnings to address.")

    else:
        print("\n❌ Environment setup is INCOMPLETE!")
        print("   Please fix the errors listed above.")

    print("\n" + "=" * 70 + "\n")

    return all_good and not errors

if __name__ == "__main__":
    try:
        success = verify_environment()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Verification failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

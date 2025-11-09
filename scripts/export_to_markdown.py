#!/usr/bin/env python3
"""
Export content items to readable Markdown files for review.

Usage:
    python3 scripts/export_to_markdown.py [--source drafts|data] [--output-dir PATH]

This script reads items from JSON files and creates individual .md files
for each item using the review template.
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime

def load_json(file_path):
    """Load and parse JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in {file_path}: {e}")
        return None

def format_review_comments(review_data, review_type):
    """Format review comments for markdown."""
    if not review_data or review_type not in review_data:
        return "_No comments yet_\n"

    comments = review_data[review_type]
    if not comments:
        return "_No comments yet_\n"

    output = []
    for comment in comments:
        severity_icon = {
            'low': '🟢',
            'medium': '🟡',
            'high': '🔴'
        }.get(comment.get('severity', 'low'), '⚪')

        disposition_icon = {
            'open': '🔵',
            'accepted': '✅',
            'rejected': '❌'
        }.get(comment.get('disposition', 'open'), '⚪')

        output.append(f"#### {severity_icon} {disposition_icon} Comment by {comment.get('author', 'Unknown')}")
        output.append(f"**Field**: `{comment.get('field', 'general')}`  ")
        output.append(f"**Severity**: {comment.get('severity', 'low').capitalize()}  ")
        output.append(f"**Status**: {comment.get('disposition', 'open').capitalize()}  ")
        output.append(f"\n{comment.get('comment', '')}\n")

        if comment.get('proposed'):
            output.append(f"**Proposed Change**:")
            output.append(f"```")
            output.append(str(comment['proposed']))
            output.append(f"```\n")

    return '\n'.join(output) if output else "_No comments yet_\n"

def export_item_to_markdown(item, group_key, template_path, output_path):
    """Export a single item to markdown using template."""

    # Read template
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
    except FileNotFoundError:
        print(f"❌ Error: Template not found: {template_path}")
        return False

    # Extract data
    header = item.get('header', 'Untitled')
    content_short = item.get('contentShort', '')
    content_long = item.get('contentLong', '')
    keywords = item.get('keywords', '')
    image_prompt = item.get('imagePrompt', '_No image prompt specified_')
    image_path = item.get('imagePath', '')
    status = item.get('status', 'UNKNOWN')
    status_reason = item.get('statusReason', '_No reason provided_')

    # Format review comments
    review = item.get('review', {})
    medical_comments = format_review_comments(review, 'medical')
    product_comments = format_review_comments(review, 'product')
    context_comments = format_review_comments(review, 'context')

    # Replace template placeholders
    content = template.replace('{HEADER}', header)
    content = content.replace('{ID}', item.get('id', 'unknown'))
    content = content.replace('{STATUS}', status)
    content = content.replace('{REVISION}', str(item.get('revision', 1)))
    content = content.replace('{CREATED_DATE}', item.get('createdDate', 'unknown'))
    content = content.replace('{CREATED_BY}', item.get('createdBy', 'unknown'))
    content = content.replace('{UPDATED_DATE}', item.get('updatedDate', 'unknown'))
    content = content.replace('{UPDATED_BY}', item.get('updatedBy', 'unknown'))
    content = content.replace('{LABEL}', item.get('label', 'unknown'))
    content = content.replace('{GROUP_KEY}', group_key)
    content = content.replace('{INDEX}', str(item.get('index', 0)))
    content = content.replace('{HEADER_LENGTH}', str(len(header)))
    content = content.replace('{SHORT_LENGTH}', str(len(content_short)))
    content = content.replace('{CONTENT_SHORT}', content_short)
    content = content.replace('{CONTENT_LONG}', content_long)
    content = content.replace('{KEYWORDS}', keywords)
    content = content.replace('{IMAGE_PROMPT}', image_prompt)
    content = content.replace('{IMAGE_PATH}', image_path)
    content = content.replace('{STATUS_REASON}', status_reason)
    content = content.replace('{MEDICAL_COMMENTS}', medical_comments)
    content = content.replace('{PRODUCT_COMMENTS}', product_comments)
    content = content.replace('{CONTEXT_COMMENTS}', context_comments)

    # Write to file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except IOError as e:
        print(f"❌ Error writing file {output_path}: {e}")
        return False

def sanitize_filename(text):
    """Create safe filename from text."""
    # Remove or replace unsafe characters
    safe = text.replace('/', '-').replace('\\', '-').replace(':', '-')
    safe = safe.replace('?', '').replace('*', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
    safe = safe.strip()
    # Limit length
    if len(safe) > 100:
        safe = safe[:100]
    return safe

def main():
    # Parse arguments
    source = 'drafts'  # default
    output_dir = None

    if '--source' in sys.argv:
        idx = sys.argv.index('--source')
        if idx + 1 < len(sys.argv):
            source = sys.argv[idx + 1]

    if '--output-dir' in sys.argv:
        idx = sys.argv.index('--output-dir')
        if idx + 1 < len(sys.argv):
            output_dir = sys.argv[idx + 1]

    # Default output directory
    if not output_dir:
        output_dir = f"exports/markdown_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    # Determine source file
    if source == 'drafts':
        source_file = 'drafts/suggestion-EN.next.json'
    elif source == 'data':
        source_file = 'data/suggestion-EN.json'
    else:
        print(f"❌ Invalid source: {source}. Use 'drafts' or 'data'.")
        sys.exit(1)

    print(f"\n📄 Exporting content to Markdown")
    print(f"📂 Source: {source_file}")
    print(f"📁 Output: {output_dir}\n")

    # Load data
    data = load_json(source_file)
    if not data or 'data' not in data:
        print("❌ No data found in source file")
        sys.exit(1)

    # Create output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Template path
    template_path = 'templates/CONTENT_REVIEW_TEMPLATE.md'

    # Export items
    total_exported = 0
    for group in data['data']:
        group_key = group.get('key', 'unknown')
        items = group.get('suggestionItem', [])

        for item in items:
            header = item.get('header', 'Untitled')
            item_id = item.get('id', 'unknown')

            # Create filename
            safe_header = sanitize_filename(header)
            filename = f"{safe_header}_{item_id[:8]}.md"
            output_path = os.path.join(output_dir, filename)

            # Export
            if export_item_to_markdown(item, group_key, template_path, output_path):
                print(f"✅ Exported: {filename}")
                total_exported += 1
            else:
                print(f"❌ Failed: {filename}")

    print(f"\n✨ Export complete!")
    print(f"📊 Total exported: {total_exported} items")
    print(f"📁 Location: {output_dir}\n")

if __name__ == '__main__':
    main()

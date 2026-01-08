#!/usr/bin/env python3
"""
Fix markdown list spacing issues.

This script ensures proper blank lines before and after lists in markdown files,
following the flow-cli DOCUMENTATION-MAKING-GUIDE.md standards.

Rules:
- Blank line after header before list
- Blank line after list before header
- Blank line after list before paragraph
"""

import re
from pathlib import Path
from typing import List


def is_header(line: str) -> bool:
    """Check if line is a markdown header."""
    return bool(re.match(r'^#{1,6}\s+', line.strip()))


def is_list_item(line: str) -> bool:
    """Check if line is a list item (unordered or ordered)."""
    stripped = line.strip()
    # Unordered list: -, *, +
    if re.match(r'^[-*+]\s+', stripped):
        return True
    # Ordered list: 1., 2., etc.
    if re.match(r'^\d+\.\s+', stripped):
        return True
    return False


def is_blank(line: str) -> bool:
    """Check if line is blank or whitespace only."""
    return line.strip() == ''


def is_code_fence(line: str) -> bool:
    """Check if line is a code fence marker."""
    return bool(re.match(r'^```', line.strip()))


def fix_spacing(lines: List[str]) -> List[str]:
    """
    Fix spacing issues in markdown content.

    Returns new list of lines with proper spacing.
    """
    result = []
    i = 0
    in_code_block = False

    while i < len(lines):
        line = lines[i]

        # Track code blocks (don't modify spacing inside them)
        if is_code_fence(line):
            in_code_block = not in_code_block
            result.append(line)
            i += 1
            continue

        # Don't modify spacing inside code blocks
        if in_code_block:
            result.append(line)
            i += 1
            continue

        # Add current line
        result.append(line)

        # Check if we need to add blank line after current line
        if i + 1 < len(lines):
            current = line
            next_line = lines[i + 1]

            # Rule 1: Header followed by list → need blank line
            if is_header(current) and is_list_item(next_line):
                if not is_blank(current):  # Only if header isn't already blank
                    result.append('\n')

            # Rule 2: List followed by header → need blank line
            elif is_list_item(current) and is_header(next_line):
                result.append('\n')

            # Rule 3: List followed by non-blank, non-list paragraph → need blank line
            elif is_list_item(current) and not is_blank(next_line) and not is_list_item(next_line) and not is_header(next_line):
                # Check if next line is actual content (not just formatting like ---)
                if not re.match(r'^[-=]{3,}$', next_line.strip()):
                    result.append('\n')

        i += 1

    return result


def process_file(file_path: Path) -> bool:
    """
    Process a single markdown file.

    Returns True if file was modified, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_lines = f.readlines()

        fixed_lines = fix_spacing(original_lines)

        # Check if anything changed
        if original_lines == fixed_lines:
            return False

        # Write back fixed content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(fixed_lines)

        return True

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def find_markdown_files(base_dir: Path) -> List[Path]:
    """Find all markdown files in the given directory and subdirectories."""
    return list(base_dir.glob('**/*.md'))


def main():
    """Main entry point."""
    # Base directory
    base_dir = Path(__file__).parent.parent
    docs_dir = base_dir / 'docs'

    # Find all markdown files
    md_files = find_markdown_files(docs_dir)

    # Also check plugin docs directories
    for plugin_dir in ['rforge', 'craft', 'statistical-research', 'workflow']:
        plugin_docs = base_dir / plugin_dir / 'docs'
        if plugin_docs.exists():
            md_files.extend(find_markdown_files(plugin_docs))

    print(f"Found {len(md_files)} markdown files to process...")

    modified_count = 0
    for md_file in md_files:
        if process_file(md_file):
            modified_count += 1
            print(f"✓ Fixed: {md_file.relative_to(base_dir)}")

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Total files: {len(md_files)}")
    print(f"  Modified: {modified_count}")
    print(f"  Unchanged: {len(md_files) - modified_count}")
    print(f"{'='*60}")

    if modified_count > 0:
        print("\nNext steps:")
        print("  1. Review changes: git diff")
        print("  2. Test build: mkdocs build")
        print("  3. Commit: git add . && git commit -m 'docs: fix markdown list spacing'")


if __name__ == '__main__':
    main()

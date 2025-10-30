#!/usr/bin/env python3
"""
Deduplicate existing transcript files
Removes consecutive duplicate lines from transcript text files
"""

import os
import sys
from pathlib import Path

def deduplicate_file(file_path):
    """
    Remove consecutive duplicate lines from a file

    Args:
        file_path: Path to the text file

    Returns:
        dict: {
            'file': str,
            'original_lines': int,
            'deduplicated_lines': int,
            'duplicates_removed': int
        }
    """

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    original_count = len(lines)

    # Remove consecutive duplicates
    deduplicated_lines = []
    prev_line = None

    for line in lines:
        if line != prev_line:
            deduplicated_lines.append(line)
            prev_line = line

    deduplicated_count = len(deduplicated_lines)
    duplicates_removed = original_count - deduplicated_count

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(deduplicated_lines))

    return {
        'file': os.path.basename(file_path),
        'original_lines': original_count,
        'deduplicated_lines': deduplicated_count,
        'duplicates_removed': duplicates_removed
    }


def deduplicate_directory(directory):
    """
    Deduplicate all .txt files in a directory

    Args:
        directory: Path to directory containing transcript files
    """

    txt_files = list(Path(directory).glob('*.txt'))

    if not txt_files:
        print(f"No .txt files found in {directory}")
        return

    print(f"Found {len(txt_files)} transcript files to deduplicate")
    print("=" * 60)

    total_duplicates_removed = 0
    results = []

    for txt_file in txt_files:
        result = deduplicate_file(txt_file)
        results.append(result)

        if result['duplicates_removed'] > 0:
            print(f"✓ {result['file']}")
            print(f"  Original: {result['original_lines']} lines")
            print(f"  Deduplicated: {result['deduplicated_lines']} lines")
            print(f"  Removed: {result['duplicates_removed']} duplicate lines")
        else:
            print(f"- {result['file']} (no duplicates found)")

        total_duplicates_removed += result['duplicates_removed']

    print("=" * 60)
    print(f"SUMMARY:")
    print(f"  Files processed: {len(results)}")
    print(f"  Total duplicate lines removed: {total_duplicates_removed}")
    print("=" * 60)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        # Default to current directory
        directory = "."

    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        sys.exit(1)

    deduplicate_directory(directory)

import os
import sys
import argparse

# CLI argument parsing
parser = argparse.ArgumentParser(description="Simplified implementation of wc")
parser.add_argument("paths", nargs="*", default=["."], help="One or more file or directory paths")
parser.add_argument("-l", "--line", action="store_true", help="Count lines")
parser.add_argument("-w", "--word", action="store_true", help="Count words")
parser.add_argument("-c", "--character", action="store_true", help="Count characters")

args = parser.parse_args()

# If no flags are set, show all
show_all = not (args.line or args.word or args.character)

# Count content in a string
def count_content(content):
    lines = content.splitlines()
    words = content.strip().split()
    characters = len(content)
    return len(lines), len(words), characters

# Format output line based on flags
def format_output(lines, words, chars, label):
    parts = []
    if args.line or show_all:
        parts.append(f"{lines:8}")
    if args.word or show_all:
        parts.append(f"{words:8}")
    if args.character or show_all:
        parts.append(f"{chars:8}")
    parts.append(label)
    return " ".join(parts)

# Totals for multiple files
total = {"lines": 0, "words": 0, "characters": 0}
file_count = 0

for input_path in args.paths:
    try:
        if os.path.isdir(input_path):
            print(f"{input_path} is a directory. Skipping.")
            continue

        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read()

        lines, words, characters = count_content(content)

        total["lines"] += lines
        total["words"] += words
        total["characters"] += characters
        file_count += 1

        print(format_output(lines, words, characters, input_path))

    except Exception as e:
        print(f'Error reading "{input_path}": {e}', file=sys.stderr)

# Print totals if more than one file processed
if file_count > 1:
    print(format_output(
        total["lines"],
        total["words"],
        total["characters"],
        "total"
    ))

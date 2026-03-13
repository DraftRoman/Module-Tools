#!/usr/bin/env python3

import os
import sys
import argparse

parser = argparse.ArgumentParser(
    prog="ls",
    description="Simple reimplementation of ls",
)

parser.add_argument(
    "-1",
    dest="one_per_line",
    action="store_true",
    help="List one entry per line",
)

parser.add_argument(
    "-a",
    dest="all_files",
    action="store_true",
    help="Do not ignore entries starting with .",
)

# Optional path (default = current directory)
parser.add_argument(
    "path",
    nargs="?",
    default=".",
    help="Directory to list (default: current directory)",
)

args = parser.parse_args()

# Get all items in the directory
try:
    entries = os.listdir(args.path)
except FileNotFoundError:
    sys.stderr.write(f"ls: cannot access '{args.path}': No such file or directory\n")
    sys.exit(1)

# Handle -a (hidden files)
if not args.all_files:
    entries = [e for e in entries if not e.startswith(".")]

# Sort for stable behaviour
entries.sort()

# Output: -1 = one per line
if args.one_per_line:
    for entry in entries:
        print(entry)
else:
    # default: space-separated
    print(" ".join(entries))

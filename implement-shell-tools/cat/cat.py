#!/usr/bin/env python3

import sys
import argparse

# Create the argument parser – similar style to `count-containing-words`
parser = argparse.ArgumentParser(
    prog="cat",
    description="Prints the contents of one or more files",
)

# positional argument: one or more paths
parser.add_argument(
    "paths",
    nargs="+",
    help="The file(s) to print",
)

args = parser.parse_args()

# Loop over each path and print its content
for path in args.paths:
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                # print line exactly as it appears in the file
                sys.stdout.write(line)
    except FileNotFoundError:
        # match shell cat-style error message
        sys.stderr.write(f"cat: {path}: No such file or directory\n")

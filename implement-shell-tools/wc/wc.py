#!/usr/bin/env python3

import argparse
import sys
import os

parser = argparse.ArgumentParser(
    prog="wc",
    description="Simple reimplementation of wc"
)

parser.add_argument(
    "-l",
    dest="count_lines",
    action="store_true",
    help="Print the line counts"
)

parser.add_argument(
    "-w",
    dest="count_words",
    action="store_true",
    help="Print the word counts"
)

parser.add_argument(
    "-c",
    dest="count_bytes",
    action="store_true",
    help="Print the byte counts"
)

parser.add_argument(
    "paths",
    nargs="+",
    help="File(s) to process"
)

args = parser.parse_args()


def wc_file(path):
    """Return (lines, words, bytes) for a file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        sys.stderr.write(f"wc: {path}: No such file or directory\n")
        return None

    lines = content.count("\n") + (1 if content and not content.endswith("\n") else 0)
    words = len(content.split())
    bytes_ = len(content.encode("utf-8"))

    return lines, words, bytes_


# If no flags are supplied, show all three
show_all = not (args.count_lines or args.count_words or args.count_bytes)

totals = [0, 0, 0]  # lines, words, bytes
multiple_files = len(args.paths) > 1

for path in args.paths:
    result = wc_file(path)
    if result is None:
        continue

    lines, words, bytes_ = result

    totals[0] += lines
    totals[1] += words
    totals[2] += bytes_

    output_parts = []

    if show_all:
        output_parts.extend([str(lines), str(words), str(bytes_)])
    else:
        if args.count_lines:
            output_parts.append(str(lines))
        if args.count_words:
            output_parts.append(str(words))
        if args.count_bytes:
            output_parts.append(str(bytes_))

    output_parts.append(path)
    print(" ".join(output_parts))


# If multiple files → print total line
if multiple_files:
    totals_output = []

    if show_all:
        totals_output.extend([str(totals[0]), str(totals[1]), str(totals[2])])
    else:
        if args.count_lines:
            totals_output.append(str(totals[0]))
        if args.count_words:
            totals_output.append(str(totals[1]))
        if args.count_bytes:
            totals_output.append(str(totals[2]))

    totals_output.append("total")
    print(" ".join(totals_output))

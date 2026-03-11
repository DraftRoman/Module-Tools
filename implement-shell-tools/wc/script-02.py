#!/usr/bin/env python3
import argparse
import sys


def count_file(path):
    """Return (lines, words, bytes) for the given file."""
    try:
        with open(path, "rb") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"wc: {path}: No such file or directory", file=sys.stderr)
        return None

    text = content.decode("utf-8", errors="replace")
    lines = text.count("\n")
    words = len(text.split())
    bytes_ = len(content)

    return lines, words, bytes_


def print_result(counts, path, show_l, show_w, show_c):
    """Format and print output for a file."""
    lines, words, bytes_ = counts

    # If no specific flag is given → print all three (like wc)
    if not (show_l or show_w or show_c):
        print(f"{lines:>7} {words:>7} {bytes_:>7} {path}")
        return

    out = []
    if show_l:
        out.append(f"{lines:>7}")
    if show_w:
        out.append(f"{words:>7}")
    if show_c:
        out.append(f"{bytes_:>7}")

    print(" ".join(out), path)


def main():
    parser = argparse.ArgumentParser(description="Simple wc implementation")
    parser.add_argument("-l", action="store_true", help="count lines")
    parser.add_argument("-w", action="store_true", help="count words")
    parser.add_argument("-c", action="store_true", help="count bytes")
    parser.add_argument("paths", nargs="+", help="file(s) to process")

    args = parser.parse_args()

    total_lines = total_words = total_bytes = 0
    multiple_files = len(args.paths) > 1

    for path in args.paths:
        result = count_file(path)
        if result is None:
            continue

        lines, words, bytes_ = result
        print_result(result, path, args.l, args.w, args.c)

        total_lines += lines
        total_words += words
        total_bytes += bytes_

    # Print totals if more than one file
    if multiple_files:
        if not (args.l or args.w or args.c):
            print(f"{total_lines:>7} {total_words:>7} {total_bytes:>7} total")
        else:
            out = []
            if args.l:
                out.append(f"{total_lines:>7}")
            if args.w:
                out.append(f"{total_words:>7}")
            if args.c:
                out.append(f"{total_bytes:>7}")
            print(" ".join(out), "total")


if __name__ == "__main__":
    main()

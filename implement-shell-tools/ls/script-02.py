#!/usr/bin/env python3

import os
import sys
import argparse


def list_directory(path, show_all):
    """List contents of a directory, respecting the -a and -1 options."""

    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"ls: cannot access '{path}': No such file or directory", file=sys.stderr)
        return

    # If -a is not provided, hide dotfiles
    if not show_all:
        entries = [e for e in entries if not e.startswith(".")]

    # Sort alphabetically like ls normally does
    entries.sort()

    # Print one entry per line (-1 behaviour)
    for entry in entries:
        print(entry)


def main():
    parser = argparse.ArgumentParser(description="Simple ls implementation")
    parser.add_argument(
        "-a",
        action="store_true",
        help="include directory entries whose names begin with a dot",
    )
    parser.add_argument(
        "-1",
        dest="one_per_line",
        action="store_true",
        help="list one file per line",
    )
    parser.add_argument("path", nargs="?", default=".", help="directory to list")

    args = parser.parse_args()

    # Only -1 is supported, but it's always required in this assignment
    if not args.one_per_line:
        print("This program only supports the -1 option.", file=sys.stderr)
        sys.exit(1)

    list_directory(args.path, show_all=args.a)


if __name__ == "__main__":
    main()

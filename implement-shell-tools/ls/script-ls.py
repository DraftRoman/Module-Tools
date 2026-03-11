#!/usr/bin/env python3

import os
import sys
import argparse


def list_directory(path, show_all, one_per_line):
    try:
        # If path is a file, just print it
        if os.path.isfile(path):
            print(path)
            return

        # If path is a directory, list its contents
        if os.path.isdir(path):
            entries = os.listdir(path)
        else:
            print(
                f"ls: cannot access '{path}': No such file or directory",
                file=sys.stderr,
            )
            return

    except PermissionError:
        print(
            f"ls: cannot open directory '{path}': Permission denied",
            file=sys.stderr,
        )
        return

    # Hide dotfiles unless -a is used
    if not show_all:
        entries = [e for e in entries if not e.startswith(".")]

    entries.sort()

    # Output formatting
    if one_per_line:
        for entry in entries:
            print(entry)
    else:
        print(" ".join(entries))


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

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="directory or file to list",
    )

    args = parser.parse_args()

    list_directory(
        args.path,
        show_all=args.a,
        one_per_line=args.one_per_line,
    )


if __name__ == "__main__":
    main()

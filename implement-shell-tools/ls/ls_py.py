#!/usr/bin/env python3

import argparse
import os
import sys


# Set up the argument parser
def parse_args():
    parser  = argparse.ArgumentParser(
        prog="list_files_in_directory",
        description="Implement ls commands to list files in directory"
    )

    parser.add_argument(
        "-1","--file-per-line",
        action="store_true",
        dest="file_per_line",
        help="list files one per line"
    )

    parser.add_argument(
        "-a",
        "--files-and-hidden-ones",
        action="store_true",
        dest="files_and_hidden_ones",
        help="list all files including hidden ones",
    )

    parser.add_argument(
        "paths",
        nargs="*",
        help="directories to list"
    )

    return parser.parse_args()

# if no paths, default to current directory
def get_paths(args):
    if len(args.paths) == 0:
        return ["."]
    return args.paths

# list a single directory
def list_directory(directory_path, show_hidden, file_per_line):
    try:
        entries = os.listdir(directory_path)
    except OSError as err:
        print(f"ls: cannot access '{directory_path}': {err}", file=sys.stderr)
        return

    if not show_hidden:
        entries = [name for name in entries if not name.startswith(".")]

    if file_per_line:
        for name in entries:
            print(name)
    else:
        print(" ".join(entries))

def main():
    args = parse_args()
    paths = get_paths(args)

    for directory_path in paths:
        list_directory(
            directory_path=directory_path,
            show_hidden=args.files_and_hidden_ones,
            file_per_line=args.file_per_line,
        )

if __name__ == "__main__":
    main()

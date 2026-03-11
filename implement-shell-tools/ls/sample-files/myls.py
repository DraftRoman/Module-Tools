#!/usr/bin/env python3
import argparse
import os

def list_directory(dir_path, show_all):
    if not os.path.exists(dir_path):
        print(f"ls: cannot access '{dir_path}': No such file or directory")
        return

    if os.path.isfile(dir_path):
        print(dir_path)
        return

    try:
        entries = os.listdir(dir_path)
    except PermissionError:
        print(f"ls: cannot access '{dir_path}': Permission denied")
        return

    if not show_all:
        entries = [e for e in entries if not e.startswith(".")]
    else:
        entries = [".", ".."] + entries

    entries.sort()
    for e in entries:
        print(e)

def main():
    parser = argparse.ArgumentParser(description="Custom implementation of ls")
    parser.add_argument("-1", action="store_true", help="list one file per line (default)")
    parser.add_argument("-a", "--all", action="store_true", help="include hidden files")
    parser.add_argument("dir", nargs="?", default=".", help="directory to list")

    args = parser.parse_args()

    list_directory(args.dir, args.all)

if __name__ == "__main__":
    main()

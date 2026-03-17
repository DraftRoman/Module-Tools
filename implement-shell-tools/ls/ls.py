import argparse
import os
import sys

parser = argparse.ArgumentParser(
    prog="ls",
    description="List all the files in a directory"
)


parser.add_argument("-a", "--all",action="store_true", help="Include hidden files")
parser.add_argument("-1", "--one", action="store_true",help="One entry per line")
parser.add_argument("dir", nargs="?" ,default=".", help="directory to list")


args = parser.parse_args()


try:
    # Gets all file names (including hidden ones)
    files = os.listdir(args.dir)
except (FileNotFoundError, NotADirectoryError) as err:
    print(f"ls: can't access: '{args.dir}': {err}")
    sys.exit(1)

visible_names = [
    entry for entry in files
    if args.all or not entry.startswith(".")
]

visible_names.sort()

if args.one:
    print("\n".join(visible_names))
else:
    print("\t".join(visible_names))
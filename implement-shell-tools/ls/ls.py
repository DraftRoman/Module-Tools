import argparse
import os

parser = argparse.ArgumentParser(
    prog="ls.py",
    description="List files in a directory"
    )

parser.add_argument("-a", action="store_true", help="Include hidden files")
parser.add_argument("directory", nargs="?", default=".", help="Directory to list")

args = parser.parse_args()

# Read files
files = os.listdir(args.directory)

# Filter if -a not given
if not args.a:
    files = [f for f in files if not f.startswith(".")]

# Print each file on a new line (like ls -1)
for f in sorted(files):
    print(f)

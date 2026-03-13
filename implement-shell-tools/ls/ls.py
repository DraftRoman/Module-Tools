import os
import argparse

parser = argparse.ArgumentParser(prog="ls", description="Lists contents of a directory")

parser.add_argument("-1", dest="one_column", action="store_true", help="List one file per line")
parser.add_argument("-a", "--all", action="store_true", help="Include hidden files")
parser.add_argument("paths", nargs='*', default=["."], help="Directories to list")

args = parser.parse_args()

for path in args.paths:
    if len(args.paths) > 1:
        print(f"{path}:")

    try:
        files = os.listdir(path)
        if not args.all:
            files = [f for f in files if not f.startswith('.')]
        
        files.sort()

        sep = "\n" if args.one_column else "  "
        print(sep.join(files))
        
        if len(args.paths) > 1:
            print()
            
    except FileNotFoundError:
        print(f"ls: cannot access '{path}': No such file or directory")

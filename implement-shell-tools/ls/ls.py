import argparse
import os

parser = argparse.ArgumentParser(
    prog="list-files-in-directory",
    description="List all files and directories in a directory",
)

parser.add_argument("-1", "--one", dest="one", help="Output one entry per line", action="store_true")
parser.add_argument("-a", help="List all files & directories, including hidden ones", action="store_true")
parser.add_argument("paths", nargs="*", default=["."], help="The file(s) or directories to list")

args = parser.parse_args()

for path in args.paths:
    if os.path.isdir(path):
        items = os.listdir(path)

        if args.a:
            items = ['.', '..'] + items
        else:
            items = [item for item in items if not item.startswith(".")]

        items.sort()
        
        for item in items:
            if args.one:
                print(item)
            else:
                print(item, end="\t")
        if not args.one:
            print()
    else:
        print(path)
   
    





    

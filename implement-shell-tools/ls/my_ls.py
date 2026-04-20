import argparse
import os

parser = argparse.ArgumentParser(
    prog="my_ls",
    description="The re-implementation of the ls command",
    epilog="Example usage: my_ls -l"
)

parser.add_argument("folders", nargs="*", help="folders to list", default=["."])
parser.add_argument("-1", action="store_true", dest="one", help="list one file per line")
parser.add_argument("-a", action="store_true", help="do not ignore entries starting with .")

args = parser.parse_args()

for folder in args.folders:
    files = os.listdir(folder)
    if args.a:
        files = [".", ".."] + files 
    else:
        files = [f for f in files if not f.startswith(".")]
     
    if args.one:
        for file in files:
            print(file)
    else:
        print(" ".join(files))



import argparse
import os 
parser=argparse.ArgumentParser(description="ls command")
parser.add_argument("-1",dest="one_per_line",action="store_true",help="List one file per line")
parser.add_argument("-a",dest="all", action="store_true",help="Include hidden files")
parser.add_argument("path", nargs="?", default=".", help="Directory to list")

args=parser.parse_args()
files=os.listdir(args.path)
if not args.all:
    new_files=[]
    for f in files:
        if not f.startswith("."):
            new_files.append(f)
    files=new_files    
if args.one_per_line:
    for f in files:
        print(f)
else:
    print(" ".join(files))        
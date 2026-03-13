import argparse
import glob


parser = argparse.ArgumentParser(description="cat command")
parser.add_argument("files", nargs="+", help="Files to read")
parser.add_argument("-n", action="store_true", help="Number all lines")
parser.add_argument("-b", action="store_true", help="Number non-empty lines")
args = parser.parse_args()


files = []
for pattern in args.files:
    files.extend(glob.glob(pattern))

line_number = 1  

for file in files:
    with open(file, "r") as f:
        for line in f:
            line_content = line.rstrip("\n")
            
            if (args.b and line_content != "") or args.n:  
                print(f"{line_number}\t{line_content}")
                line_number += 1
            else:  
                print(line_content)
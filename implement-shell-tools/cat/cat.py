import sys
import argparse

# Setup argument parser
parser = argparse.ArgumentParser(
    prog="cat",
    description="Concatenate and display files"
)

parser.add_argument("-n", "--number", action="store_true", help="Number all output lines")
parser.add_argument("-b", "--number-nonblank", action="store_true", help="Number non-empty lines only")
parser.add_argument("paths", nargs='+', help="Files to read")

args = parser.parse_args()

line_number = 1  # Shared counter across all files

for path in args.paths:
    with open(path, "r") as f:
    
        lines = f.read().splitlines()

    output = []
    for line in lines:
        if args.number_nonblank:
            if line.strip():
                output.append(f"{line_number:6}\t{line}")
                line_number += 1
            else:
                output.append(line)
        elif args.number:
            output.append(f"{line_number:6}\t{line}")
            line_number += 1
        else:
            output.append(line)

    print("\n".join(output))

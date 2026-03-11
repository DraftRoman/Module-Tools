import argparse

parser = argparse.ArgumentParser(
    prog="display-file-content",
    description="Output the content of a file to the terminal",
)

parser.add_argument("-n", help="Number the output lines", action="store_true")
parser.add_argument("-b", help="Number the non-blank output lines", action="store_true")
parser.add_argument("paths", help="The file(s)/path(s) to read from", nargs="+")

args = parser.parse_args()

line_number = 1

for path in args.paths:
    with open(path, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            if args.n:
                print(f"{line_number:>6} {line}")
                line_number += 1
            elif args.b:
                if line != "":
                    print(f"{line_number} {line}")
                    line_number += 1
                else:
                    print(f"{line}")
            else:
                print(f"{line}")









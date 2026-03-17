import argparse

parser = argparse.ArgumentParser(
    prog="cat",
    description="read, display, and concatenate text files.",
)

parser.add_argument("-n", action="store_true", help="Number all output lines.")
parser.add_argument("-b", action="store_true", help="Number non-blank output lines.")
parser.add_argument("paths",nargs="+", help="The file to search")

args = parser.parse_args()

for path in args.paths:
    try:
        with open(path, mode='r', encoding='utf-8') as f:
            lines = f.readlines()

    except Exception as err:
        print(f"Error reading file '{path}': {err}")
        continue

    line_num = 1

    for line in lines:
        if args.b:
            if line.strip() != "":
                print(f"{line_num:5} {line}", end="")
                line_num += 1
            else:
                print()
        elif args.n:
            print(f"{line_num:5} {line}", end="")
            line_num += 1
        else:
            print(line, end="")
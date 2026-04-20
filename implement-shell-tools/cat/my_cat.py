import argparse

parser = argparse.ArgumentParser(
    prog="my_cat",
    description="The re-implementation of the cat command",
    epilog="Example usage: my_cat file1.txt file2.txt -n"
)

parser.add_argument("files", nargs="+", help="files to read")
parser.add_argument("-n", "--number", action="store_true", help="number all lines")
parser.add_argument("-b", "--number-nonblank", action="store_true", help="number non-empty lines")

args = parser.parse_args()
print(args)
line_number = 1

try:
    for path in args.files:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if args.number_nonblank:
            output = []
            for line in lines:
                if line.strip() == "":
                    output.append(line.rstrip("\n"))
                else:
                    output.append(f"{line_number} {line.rstrip()}")
                    line_number += 1

        elif args.number:
            output = [
                f"{i + 1} {line.rstrip()}"
                for i, line in enumerate(lines)
            ]

        else:
            output = [line.rstrip("\n") for line in lines]

        print("\n".join(output))

except Exception as err:
    print(f"Error reading file: {err}")
    exit(1)
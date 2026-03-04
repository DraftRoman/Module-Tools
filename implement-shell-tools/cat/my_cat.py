import argparse
import sys

parser = argparse.ArgumentParser(
    description="Reads and prints one or more files, optionally numbering lines continuously"
)
parser.add_argument("paths", nargs='+', help="One or more file paths")
parser.add_argument("-n", "--number", action="store_true", help="Number all output lines")
parser.add_argument("-b", "--number-nonblank", action="store_true", help="Number non-empty output lines")

args = parser.parse_args()

file_paths = args.paths
number_nonblank = args.number_nonblank
number_all = args.number and not number_nonblank


total_lines = 0
total_nonblank_lines = 0

for path in file_paths:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            total_lines += len(lines)
            total_nonblank_lines += sum(1 for line in lines if line.strip())
    except Exception as e:
        print(f'Error reading file "{path}": {e}', file=sys.stderr)
        sys.exit(1)


if number_nonblank:
    max_digits = len(str(total_nonblank_lines))
elif number_all:
    max_digits = len(str(total_lines))

line_number = 1


for path in file_paths:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if number_nonblank:
            for line in lines:
                if line.strip() == "":
                    print()
                else:
                    num_str = str(line_number).rjust(max_digits)
                    print(f"{num_str}\t{line.rstrip()}")
                    line_number += 1

        elif number_all:
            for line in lines:
                num_str = str(line_number).rjust(max_digits)
                print(f"{num_str}\t{line.rstrip()}")
                line_number += 1

        else:
            for line in lines:
                print(line, end='')
            if lines and not lines[-1].endswith('\n'):
                print()

    except Exception as e:
        print(f'Error reading file "{path}": {e}', file=sys.stderr)
        sys.exit(1)

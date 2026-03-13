import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        prog ="display-file-content",
        description = "Implement cat command with -n and -b flag support",
        )

    parser.add_argument("-n", "--number-all-lines",
                        action="store_true",
                        help="Number every line in the file"
                        )

    parser.add_argument("-b", "--number-non-empty-lines",
                        action="store_true",
                        help="Number non empty lines in the file"
                        )

    parser.add_argument("paths", nargs="+", help="File paths to process")

    args = parser.parse_args()
    return args


def print_line(line, line_number = None):
    if line_number is None:
        print(line, end="")
    else:
        print(f"{line_number} {line}", end="")

def process_line(line, args, line_number):
    if args.number_non_empty_lines:
        if line.strip() == "":
            print_line(line)
        else:
            print_line(line, line_number)
            line_number += 1

    elif args.number_all_lines:
        print_line(line, line_number)
        line_number +=1

    else:
        print_line(line)

    return line_number

def process_file(filepath, args, line_number):
    """Read a file and print its lines. Returns updated line_number."""
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line_number = process_line(line, args, line_number)
    return line_number

def main():
    args = parse_args()
    line_number = 1

    for filepath in args.paths:
        line_number = process_file(filepath, args, line_number)

if __name__ == "__main__":
    main()

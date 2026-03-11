#!/usr/bin/env python3
import sys
import argparse

def read_file(path, number_all, number_nonblank, line_counter):
    """Reads a file and prints its contents with the requested numbering."""
    try:
        with open(path, "r") as f:
            for line in f:
                line_no_newline = line.rstrip("\n")

                if number_all:
                    print(f"{line_counter:6}\t{line_no_newline}")
                    line_counter += 1

                elif number_nonblank:
                    if line_no_newline.strip():
                        print(f"{line_counter:6}\t{line_no_newline}")
                        line_counter += 1
                    else:
                        print("")  # blank line stays blank

                else:
                    print(line_no_newline)

        return line_counter

    except FileNotFoundError:
        print(f"cat: {path}: No such file or directory", file=sys.stderr)
        return line_counter


def main():
    parser = argparse.ArgumentParser(description="Simple cat implementation")
    parser.add_argument("-n", action="store_true", help="number all lines")
    parser.add_argument("-b", action="store_true", help="number non-blank lines")
    parser.add_argument("files", nargs="+", help="files to read")

    args = parser.parse_args()

    # cat rule: if -b is used, ignore -n
    number_all = args.n
    number_nonblank = args.b
    if number_nonblank:
        number_all = False

    line_counter = 1

    for path in args.files:
        line_counter = read_file(path, number_all, number_nonblank, line_counter)


if __name__ == "__main__":
    main()

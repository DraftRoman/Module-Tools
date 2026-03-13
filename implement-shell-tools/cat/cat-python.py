import sys
import argparse

def cat_file(filename, flag):
    try:
        with open(filename, 'r') as file:
            if not flag:
                for line in file:
                    print(line, end="")

            elif flag == "-n":
                for index, line in enumerate(file, start=1):
                    print(f"{index:6}\t{line}", end="")

            elif flag == "-b":
                line_number = 1
                for line in file:
                    if line.strip() == "":
                        print(line, end="")
                    else:
                        print(f"{line_number:6}\t{line}", end="")
                        line_number += 1

    except FileNotFoundError:
        print(f"cat: {filename}: No such file or directory", file=sys.stderr)
    
def main():
    parser = argparse.ArgumentParser(description="Simple cat clone")

    parser.add_argument("filenames", nargs="+",
                        help="Files to display")
    parser.add_argument("-n", action="store_true",
                        help="Number all output lines")
    parser.add_argument("-b", action="store_true",
                        help="Number non-blank output lines")

    args = parser.parse_args()

    flag = False
    if args.n:
        flag = "-n"
    elif args.b:
        flag = "-b"

    for filename in args.filenames:
        cat_file(filename, flag)

if __name__ == "__main__":
    main()

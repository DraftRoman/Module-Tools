import argparse


parser = argparse.ArgumentParser(
    prog="cat",
    description="An alternative to the 'cat' command",
)

parser.add_argument("files", nargs="+", help="The file(s) to process")
parser.add_argument("-n", "--number", action="store_true", help="Number all output lines")
parser.add_argument("-b", "--number-nonblank", action="store_true", help="Number non-blank output lines")

args = parser.parse_args()



def print_line(line, padding_width, line_number=None):
    """Helper function to print a line with optional line numbering."""
    if line_number is not None:
        print(f"{str(line_number).rjust(padding_width)}  {line}")
    else:
        print(line)

line_number = 1 
padding_width = 6  

for file in args.files:
    with open(file, "r") as f:
        # read the content and split the lines ready to process as needed
        content = f.read().splitlines()

    for line in content:
        # use .strip() to remove leading and trailing whitespace or /n
        if args.number_nonblank and line.strip():
            # number non-blank lines only
            print_line(line, padding_width, line_number)
            line_number += 1
        elif args.number:
            # number all lines
            print_line(line, padding_width, line_number)
            line_number += 1
        else:
            # no flags
            print_line(line, padding_width)
# This program works like the 'cat' command in Unix.
# It reads one or more files (or input from the keyboard) and prints the content.
# You can choose to number all lines (-n) or only non-empty lines (-b).

import argparse
import sys

def setup_arguments():
    # Set up the options for the program
    parser = argparse.ArgumentParser(
        prog="cat",
        description="Concatenate and display files, optionally numbering lines."
    )

    # You can choose either to number all lines or only non-empty lines
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-n", "--number", action="store_true", help="Number all output lines, starting at 1.")
    group.add_argument("-b", "--number-nonblank", action="store_true", help="Number non-empty output lines, starting at 1.")

    # Add the file names (or '-' for keyboard input)
    parser.add_argument("paths", nargs='+', help="Files to read ('-' for stdin).")

    return parser.parse_args()

def read_file_content(path):
    # Read the content of a file or from the keyboard
    try:
        if path == "-":
            return sys.stdin.read()  # Read from keyboard or piped input
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()  # Read from file
    except Exception as e:
        # Show error if file can't be read
        print(f"Error reading {path}: {e}", file=sys.stderr)
        return ""

def extract_content_lines(content):
    # Split the text into lines
    return content.splitlines()

def output_lines(lines, number_all, number_nonblank):
    line_number = 1  # Start counting from 1
    for line in lines:
        if number_all:
            # Add a number to every line
            print(f"{line_number:6}\t{line}")
            line_number += 1
        elif number_nonblank:
            # Add a number only to lines that are not empty
            if line.strip() != "":
                print(f"{line_number:6}\t{line}")
                line_number += 1
            else:
                print()  # Print empty line without number
        else:
            # Just print the line with no number
            print(line)

def main():
    # Main function: gets the arguments, reads files, and prints them
    args = setup_arguments()
    all_lines = []

    # Go through each file and read its lines
    for path in args.paths:
        content = read_file_content(path)
        lines = extract_content_lines(content)
        all_lines.extend(lines)  # Add lines to the list

    # Print the lines with or without numbers
    output_lines(all_lines, args.number, args.number_nonblank)

# Start the program
if __name__ == "__main__":
    main()

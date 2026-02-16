import argparse

parser = argparse.ArgumentParser(
    prog="cat program implementation",
    description="Implements the cat program",
)

parser.add_argument("-n", "--number", action="store_true", help="Number the output lines, starting at 1.")
parser.add_argument("-b", "--number2", action="store_true", help="Number the output of non-empty lines, starting at 1.")
parser.add_argument("paths", nargs='+', help="The files to search")

args = parser.parse_args()
def read_file_content(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def extract_content_lines(content):
    lines = content.split('\n')
    if lines and lines[-1] == '':
        lines = lines[:-1]
    return lines

def output_lines_with_numbers(lines):
    count = 0
    number_lines = args.number
    number_non_empty_lines = args.number2
    for line in lines:
        if number_lines:
            count += 1
            print(count, line)
        elif(number_non_empty_lines) and line != '':
            count += 1
            print(count, line)
        else:
            print(line)

# Read contents of all files into a list
all_lines = []
for path in args.paths:
    content = read_file_content(path)
    lines = extract_content_lines(content)
    all_lines.extend(lines)

# Output lines with or without numbering
output_lines_with_numbers(all_lines)

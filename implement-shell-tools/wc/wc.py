import argparse
import sys

parser = argparse.ArgumentParser(
    prog="wc.py",
    description="Count lines, words, and characters in text files."
)

parser.add_argument("-l", action="store_true", help="Count lines")
parser.add_argument("-w", action="store_true", help="Count words")
parser.add_argument("-c", action="store_true", help="Count characters")

parser.add_argument("files", nargs="+", help="Text files to read")

args = parser.parse_args()

def format_output(line_count, word_count, char_count, count_lines, count_words, count_chars):
    output_list = []

     # If no flag is given, show all
    if not (count_lines or count_words or count_chars):
        output_list = [str(line_count), str(word_count), str(char_count)]

    else:
        if args.l:
            output_list.append(str(line_count))
        if args.w:
            output_list.append(str(word_count))
        if args.c:
            output_list.append(str(char_count))
            
    return output_list

# Totals for multiple files
total_lines = 0
total_words = 0
total_chars = 0

# Loop through each file
for file_path in args.files:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        line_count = content.count("\n")
        word_count = len(content.split())
        char_count = len(content)

        total_lines += line_count
        total_words += word_count
        total_chars += char_count
        
        output = format_output(line_count, word_count, char_count, args.l, args.w, args.c)

        output.append(file_path)
        print(" ".join(output))

    except FileNotFoundError:
        print(f"wc: {file_path}: No such file or directory", file=sys.stderr)
    except Exception as e:
        print(f"wc: {file_path}: Error reading file: {e}", file=sys.stderr)


# Show total only if multiple files given
if len(args.files) > 1:
    total_output = format_output(total_lines, total_words, total_chars, args.l, args.w, args.c)

    total_output.append("total")
    print(" ".join(total_output))

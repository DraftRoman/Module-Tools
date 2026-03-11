import argparse
import sys
import glob # to find file paths and match patterns

def parseargs():
    parser = argparse.ArgumentParser(
        prog = "wc",
        description = "wc clone supporting -l, -w, -c flags"
    )
    parser.add_argument("-l", "--lines", action = "store_true",help = "print line counts")
    parser.add_argument("-w", "--words", action ="store_true",help = "print word count")
    parser.add_argument("-c", "--bytes", action ="store_true", help = "print byte count")
    parser.add_argument("files", nargs="+", help="Files to read (shell globs allowed)")

    return parser.parse_args()

   #Uses glob to expand patterns like *.txt.
def expand_files(patterns):
    expanded = []
    for p in patterns:
        matches = glob.glob(p)
        if matches:
            expanded.extend(sorted(matches))  # predictable order
        else:
            print(f"wc: {p}: No such file", file=sys.stderr) #Prints an error if a pattern matches nothing.
    return expanded

def file_counts(filename):
    try:
        with open(filename, "rb") as f: #opening file in binary mode to be able to count bytes.
            data = f.read()
    except FileNotFoundError:
        print(f"wc: {filename}: No such file", file=sys.stderr)
        return None

    text = data.decode("utf-8", errors="ignore")
    line_count = text.count("\n")
    word_count = len(text.split())
    byte_count = len(data)

    return line_count, word_count, byte_count

def print_counts(filename, counts, show_lines, show_words, show_bytes): #args.lines is passed into the parameter show_lines and same for other arguments.
    line_count, word_count, byte_count = counts

    # If no flags are set, show all three
    if not (show_lines or show_words or show_bytes):
        print(f"{line_count:7} {word_count:7} {byte_count:7} {filename}")
        return

    output = []
    if show_lines:
        output.append(f"{line_count:7}") #:7 to ensure nums are rightaligned in a spaced column -just like GNU wc
    if show_words:
        output.append(f"{word_count:7}")
    if show_bytes:
        output.append(f"{byte_count:7}")
    output.append(filename)
    print(" ".join(output))

def main():
    args = parseargs()
    files = expand_files(args.files)

    total_lines, total_words, total_bytes = 0, 0, 0

    for file in files:
        counts = file_counts(file)
        if counts is None:
            continue
        print_counts(file, counts, args.lines, args.words, args.bytes)
        total_lines += counts[0]
        total_words += counts[1]
        total_bytes += counts[2]

    # If multiple files, print totals
    if len(files) > 1:
        total_counts = (total_lines, total_words, total_bytes)
        print_counts("total", total_counts, args.lines, args.words, args.bytes)

if __name__ == "__main__":
    main()
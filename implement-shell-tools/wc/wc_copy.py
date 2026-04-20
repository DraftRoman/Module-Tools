import argparse

parser = argparse.ArgumentParser(
    prog="wc_copy",
    description="The re-implementation of the wc command",
    epilog="Example usage: wc_copy file1.txt file2.txt -n"
)

parser.add_argument("files", nargs="+", help="files to read")
parser.add_argument("-l", action="store_true", help="number of the lines")
parser.add_argument("-w", action="store_true", help="print the word counts")
parser.add_argument("-c", action="store_true", help="print the byte counts")
args = parser.parse_args()
if not (args.l or args.w or args.c):
    args.l = args.w = args.c = True

try:
    for path in args.files:
        with open(path, "r", encoding="utf-8") as f:
            
            lines = f.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            byte_count = sum(len(line.encode("utf-8")) for line in lines)

        if args.l:
            print(f"{line_count} lines {path}")
        if args.w:
            print(f"{word_count} words {path}")
        if args.c:
            print(f"{byte_count} bytes {path}")

except Exception as err:
    print(f"Error reading file: {err}")
    exit(1)

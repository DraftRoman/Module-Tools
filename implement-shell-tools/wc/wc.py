import argparse
import sys
import re


def main():
    parser= argparse.ArgumentParser(
        prog="wc",
        description ="wc command implementation in python"
    )

    parser.add_argument("-l", action="store_true", help ="show number of lines only")
    parser.add_argument("-w", action="store_true", help="show number of words only")
    parser.add_argument("-c", action="store_true", help="show number of characters only")

    parser.add_argument("paths", nargs="*", help="file paths to process")

    args = parser.parse_args()

    if len(args.paths) == 0:
        print("wc: no file specified", file=sys.stderr)
        sys.exit(1)

    totals= {"lines": 0, "words": 0, "chars": 0}

    no_flags = not args.l and not args.w and not args.c
    width = 8

    def format_output(counts, label):
        if no_flags:
            return f"{counts['lines']:>{width}}{counts['words']:>{width}}{counts['chars']:>{width}} {label}"

        parts = []
        if args.l:
            parts.append(f"{counts['lines']:>{width}}")
        if args.w:
            parts.append(f"{counts['words']:>{width}}")
        if args.c:
            parts.append(f"{counts['chars']:>{width}}")

        return f"{''.join(parts)} {label}"
    had_error = False

    for file_path in args.paths:
        try:
            with open(file_path, "rb") as f:
                data = f.read()
        except OSError as err:
            print(f"wc: cannot read file' {file_path} ': {err}", file=sys.stderr)
            had_error = True
            continue

        content = data.decode("utf-8", errors="replace")

        line_count = content.count("\n")

        words = [w for w in re.split(r"\s+", content) if w]
        word_count = len(words)
        char_count = len(data)

        counts = {"lines": line_count, "words": word_count, "chars":char_count}

        totals["lines"] += line_count
        totals["words"] += word_count
        totals["chars"] +=char_count

        print(format_output(counts, file_path))

    if len(args.paths) > 1:
        print(format_output(totals, "total"))

    sys.exit(1 if had_error else 0)

if __name__ == "__main__":
    main()

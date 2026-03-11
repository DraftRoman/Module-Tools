#!/usr/bin/env python3
import argparse
import glob
import os

def count_lines(text):
    if not text:
        return 0
    lines = text.splitlines()
    return len(lines)

def count_words(text):
    return len([w for w in text.split() if w])

def count_chars(text):
    return len(text.encode('utf-8'))

def wc_file(filename, options):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"wc: {filename}: No such file")
        return None

    lines = count_lines(text)
    words = count_words(text)
    chars = count_chars(text)

    padding = 7
    if options.lines and not options.words and not options.chars:
        output = f"{lines} {filename}"
    elif options.words and not options.lines and not options.chars:
        output = f"{words} {filename}"
    elif options.chars and not options.lines and not options.words:
        output = f"{chars} {filename}"
    else:
        output = f"{str(lines).rjust(padding)} {str(words).rjust(padding)} {str(chars).rjust(padding)} {filename}"

    print(output)
    return {"lines": lines, "words": words, "chars": chars}

def main():
    parser = argparse.ArgumentParser(description="Custom implementation of wc")
    parser.add_argument("-l", "--lines", action="store_true", help="count lines")
    parser.add_argument("-w", "--words", action="store_true", help="count words")
    parser.add_argument("-c", "--chars", action="store_true", help="count characters")
    parser.add_argument("files", nargs="+", help="files or wildcard patterns")
    args = parser.parse_args()

    all_files = []
    for pattern in args.files:
        expanded = glob.glob(pattern)
        if not expanded:
            print(f"wc: {pattern}: No such file or directory")
        all_files.extend(expanded)

    total_lines = total_words = total_chars = 0

    for file in all_files:
        result = wc_file(file, args)
        if result:
            total_lines += result["lines"]
            total_words += result["words"]
            total_chars += result["chars"]

    padding = 7
    if len(all_files) > 1:
        if args.lines and not args.words and not args.chars:
            print(f"{total_lines} total")
        elif args.words and not args.lines and not args.chars:
            print(f"{total_words} total")
        elif args.chars and not args.lines and not args.words:
            print(f"{total_chars} total")
        else:
            print(f"{str(total_lines).rjust(padding)} {str(total_words).rjust(padding)} {str(total_chars).rjust(padding)} total")

if __name__ == "__main__":
    main()

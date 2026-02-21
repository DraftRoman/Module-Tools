import argparse

parser = argparse.ArgumentParser(
    prog="my-wc",
    description="Simple wc clone with -l and -w options",
)




def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def count_text(text):
    line_count = text.count("\n")
    word_count = len(text.split())
    char_count = len(text)
    return line_count, word_count, char_count




lineCounter = 0
wordCounter = 0
charCounter = 0

parser.add_argument("-l", action="store_true", help="count lines")
parser.add_argument("-w", action="store_true", help="count words")
parser.add_argument("-c", action="store_true", help="count characters")
parser.add_argument("path", nargs="+", default=".", help="The file to count")
args = parser.parse_args()



for path in args.path:
    text = read_file(path)
    lines, words, chars = count_text(text)

    lineCounter += lines
    wordCounter += words
    charCounter += chars

    if args.l:
        print(lines, path)
    elif args.w:
        print(words, path)
    elif args.c:
        print(chars, path)
    else:
        print(lines, words, chars, path)

if len(args.path) > 1:
    if args.l:
        print(lineCounter, "total")
    elif args.w:
        print(wordCounter, "total")
    elif args.c:
        print(charCounter, "total")
    else:
        print(lineCounter, wordCounter, charCounter, "total")
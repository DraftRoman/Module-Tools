import argparse
import os

parser = argparse.ArgumentParser(
    prog="wc",
    description="Display numbers of line, words, and bytes in each file"
)

parser.add_argument("-l", action="store_true", help="Number of lines")
parser.add_argument("-w", action="store_true" ,help="Number of words")
parser.add_argument("-c", action="store_true" ,help="Number of bytes")
parser.add_argument("paths", nargs="+", help="The file to search")

args = parser.parse_args()

totalLines = 0
totalWords = 0
totalBytes = 0

lines = args.l
words = args.w
bytes = args.c

for path in args.paths:
    try:
        with open(path, "r") as f:
            content = f.read()

    except Exception as err:
        print(f"Error reading file '{path}': {err}")
        continue
    
    lineCount = len(content.split("/n"))
    wordCount = len(content.split())
    byteCount = os.path.getsize(path)

    totalLines += lineCount
    totalWords += wordCount
    totalBytes += byteCount

    if lines:
        print(f"\t{lineCount} {path}")
        lineCount += 1
    elif words:
        print(f"\t{wordCount} {path}")
    elif bytes:
        print(f"\t{byteCount} {path}")
    else:
        print(f"\t{lineCount} \t{wordCount} \t{byteCount} {path}")

if len(args.paths) > 1:
    if lines:
        print(f"{totalLines} total")
    elif words:
        print(f"{totalWords} total")
    elif bytes:
        print(f"{totalBytes} total")
    else:
        print(f"\t{totalLines} \t{totalWords} \t{totalBytes} total")
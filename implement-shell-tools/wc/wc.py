
import argparse
import os

parser = argparse.ArgumentParser(
    prog="counter",
    description="Counts lines, words or characters in a file (or all files) inside a directory",
)

parser.add_argument("-l", "--line", dest="line", help="The number of lines in each file", action="store_true")
parser.add_argument("-w", "--word", dest="word", help="The number of words in each file", action="store_true")
parser.add_argument("-c", "--char", dest="char", help="The number of characters in each file", action="store_true")
parser.add_argument("paths", help="The file(s)/path(s) to read from", nargs="+")

args = parser.parse_args()

total = {'lines': 0, 'words': 0, 'characters': 0, 'files': 0}

def counter(item):
    lines = len(item.strip().split("\n"))
    words = len(item.split())
    characters = len(item)
    return {"lines": lines, "words": words, "characters": characters}


def process_file(file_path, total):
    with open(file_path, "r") as f:
        content = f.read()

    stats = counter(content)

    if args.line:
        print(f"{stats['lines']} {file_path}")
    elif args.word:
        print(f"{stats['words']} {file_path}")
    elif args.char:
        print(f"{stats['characters']} {file_path}")
    else:
        print(f"{stats['lines']} {stats['words']} {stats['characters']} {file_path}")

    total['lines'] += stats['lines']
    total['words'] += stats['words']
    total['characters'] += stats['characters']
    total['files'] += 1



for path in args.paths:
    if os.path.isfile(path):
        process_file(path, total)
    elif os.path.isdir(path):
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                process_file(file_path, total)
                   
                
    

        



if total['files'] > 1:
    if args.line:
        print(f"{total['lines']} total")
    elif args.word:
        print(f"{total['words']} total")
    elif args.char:
        print(f"{total['characters']} total")
    else:
        print(f"{total['lines']} {total['words']} {total['characters']} total")





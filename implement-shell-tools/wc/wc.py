import sys
from pathlib import Path

def calculateCounts(inputFiles):
    return {
        "lines": len(inputFiles.split("\n")) - 1,
        "words": len(inputFiles.split()),
        "bytes": len(inputFiles),
    }

# * `wc -l sample-files/3.txt`
# * `wc -l sample-files/*`
def countLines(listOfFiles):
    for file in listOfFiles:
        content = Path(file).read_text(encoding="utf-8")

        counts = calculateCounts(content)
        print(f"{counts['lines']} {file}")

# * `wc -w sample-files/3.txt`
def countWords(listOfFiles):
    for file in listOfFiles:
        content = Path(file).read_text(encoding="utf-8")

        # const wordsCounted = content.split(" ").filter(word => word !== "").length;
        counts = calculateCounts(content)
        print(f"{counts['words']} {file}")

# * `wc -c sample-files/3.txt`
def countBytes(listOfFiles):
    for file in listOfFiles:
        content = Path(file).read_text(encoding="utf-8")
        counts = calculateCounts(content)
        print(f"{counts['bytes']} {file}")

# * `wc sample-files/*`
def countAll(listOfFiles):
    for file in listOfFiles:
        content = Path(file).read_text(encoding="utf-8")
        counts = calculateCounts(content)
        print(f"{counts['lines']} {counts['words']} {counts['bytes']} {file}")

argv = sys.argv[1:]
files = [arg for arg in argv if not arg.startswith("-")]

if "-l" in argv:
    countLines(files)
elif "-w" in argv:
    countWords(files)
elif "-c" in argv:
    countBytes(files)
else:
    countAll(files)
import sys
from pathlib import Path

def countAll(listOfFiles, flag=None):
    for file in listOfFiles:
        content = Path(file).read_text(encoding="utf-8")
        if flag == "-l":
            print(f"{len(content.splitlines())} {file}")
        elif flag == "-w":
            print(f"{len(content.split())} {file}")
        elif flag == "-c":
            print(f"{len(content)} {file}")
        else:
            print(f"{len(content.splitlines())} {len(content.split())} {len(content)} {file}")

argv = sys.argv[1:]
files = [arg for arg in argv if not arg.startswith("-")]

if "-l" in argv:
    countAll(files, "-l")
elif "-w" in argv:
    countAll(files, "-w")
elif "-c" in argv:
    countAll(files, "-c")
else:
    countAll(files)
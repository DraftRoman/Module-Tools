import sys
from pathlib import Path

def cleanInput(listOfFiles):
    cleanLinesArr = []

    for file in listOfFiles:
        grabbedText = Path(file).read_text(encoding="utf-8") 
        splitLines = grabbedText.splitlines()
        cleanLinesArr.extend(splitLines) 
    
    return cleanLinesArr

def takeSpecifiedAction(cleanLinesArr, flag):
    countingOnlyFullLines = 1

    if flag not in (None, "-n", "-b"):
        print("incorrect flag")
        return

    for line in cleanLinesArr: 
        if not flag:
            print(line)
        elif flag == "-n":
            print(f"{countingOnlyFullLines} {line}")
            countingOnlyFullLines += 1
        elif flag == "-b":
            if line == "":
                print("")
            else:
                print(f"{countingOnlyFullLines} {line}")
                countingOnlyFullLines += 1


args = sys.argv[1:]  
flag = None
restIsFiles = []

if len(args) > 0 and args[0] and args[0][0] == "-":
    flag = args[0]
    restIsFiles = args[1:]
else:
    flag = None
    restIsFiles = args

lines = cleanInput(restIsFiles)
takeSpecifiedAction(lines, flag)
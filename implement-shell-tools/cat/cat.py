import sys
from pathlib import Path

def cleanInput(listOfFiles):
    cleanLinesArr = []

    for file in listOfFiles:
        grabbedText = Path(file).read_text(encoding="utf-8") 
        splitLines = grabbedText.split("\n")
        cleanLinesArr.extend(splitLines) 
    
    return cleanLinesArr

args = sys.argv[1:]  
flag = None
restIsFiles = []

if len(args) > 0 and args[0] and args[0][0] == "-":
    flag = args[0]
    restIsFiles = args[1:]
else:
    flag = None
    restIsFiles = args

def takeSpecifiedAction(cleanLinesArr, flag):
    countingOnlyFullLines = 1

    for file in cleanLinesArr: 
        if not flag:
            print(file)
        elif flag == "-n":
            print(f"{countingOnlyFullLines} {file}")
            countingOnlyFullLines += 1
        elif flag == "-b":
            if file == "":
                print("")
            else:
                print(f"{countingOnlyFullLines} {file}")
                countingOnlyFullLines += 1
        else:
            print("incorrect flag")

lines = cleanInput(restIsFiles)
takeSpecifiedAction(lines, flag)
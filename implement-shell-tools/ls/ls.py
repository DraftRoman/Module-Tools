import sys
import os

#  `ls -1`
def showAllFilesInDir(directory):
    listOfFiles = os.listdir(directory)

    for eachFile in listOfFiles:
        if eachFile[0] != ".":
            print(eachFile)

# `ls -1 sample-files`
def showVisibleInSampleFiles():
    listOfFiles = os.listdir("sample-files")

    for eachFile in listOfFiles:
        if eachFile[0] != ".":
            print(eachFile)

# `ls -1 -a sample-files`
def showAllInSampleFiles():
    listOfFiles = os.listdir("sample-files")

    for eachFile in listOfFiles:
        print(eachFile)

argv = sys.argv[1:]

if "-a" in argv:
    showAllInSampleFiles()
elif "sample-files" in argv:
    showVisibleInSampleFiles()
else:
    showAllFilesInDir(".")
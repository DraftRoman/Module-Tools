import sys
import os

#  `ls -1`
def showAllFilesInDir(directory):
    listOfFiles = os.listdir(directory)

    for eachFile in listOfFiles:
        if eachFile[0] != ".":
            print(eachFile)

# `ls -1 sample-files`
def showVisibleInSampleFiles(directory):
    listOfFiles = os.listdir(directory)

    for eachFile in listOfFiles:
        if eachFile[0] != ".":
            print(eachFile)

# `ls -1 -a sample-files`
def showAllInSampleFiles(directory):
    listOfFiles = os.listdir(directory)

    for eachFile in listOfFiles:
        print(eachFile)

argv = sys.argv[1:]

show_all = "-a" in argv

directories = [arg for arg in argv if arg != "-a"]
if not directories:
    directories = ["."]
    
for directory in directories:
    if show_all:
        showAllInSampleFiles(directory)
    else:
        showVisibleInSampleFiles(directory)
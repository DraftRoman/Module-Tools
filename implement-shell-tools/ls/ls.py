import argparse
import os


def show_files(files, show_hidden):
    for file in files:
        if show_hidden or not file.startswith("."):
             print(file)


parser = argparse.ArgumentParser(
    prog="my-ls",
    description="Simple ls clone with -a and -l options",
)

parser.add_argument("-a", action="store_true", help="include hidden files")
parser.add_argument(
    "-1", dest="one", action="store_true", help="list one entry per line"
)
parser.add_argument("path", nargs="?", default=".", help="The directory to list")
args = parser.parse_args()


directory_path = args.path
listDir = os.listdir(directory_path)


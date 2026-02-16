import argparse
import os


parser = argparse.ArgumentParser(
    prog="The ls program",
    description="Implements the ls program"
)
parser.add_argument('dir', nargs='?', type=str, help="Path to the directory to list", default='.')
parser.add_argument("-1", "--one", action="store_true", help="list the directory files one per line")

parser.add_argument("-a", "--hidden_files", action="store_true", help="list the directory files one per line")

args = parser.parse_args()


def list_directory_contents():
    is_file_per_line_option = args.one
    is_hidden_option = args.hidden_files
    dir = args.dir
    files = os.listdir(dir)

    if is_hidden_option:
        files = ['.', '..'] + files

    for file in files:
        if is_hidden_option or not file.startswith('.'):
            if is_file_per_line_option:
                print(file)
            else:
                print(file, end=' ')
    if not is_file_per_line_option:
        print()

list_directory_contents()
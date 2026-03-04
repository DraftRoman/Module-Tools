import os
import sys
import stat
import argparse

parser = argparse.ArgumentParser(
    description="List files in a directory (simplified ls implementation)"
)
parser.add_argument("paths", nargs="*", default=["."], help="One or more file or directory paths")
parser.add_argument("-l", "--longList", action="store_true", help="Long listing format")
parser.add_argument("-a", "--all", action="store_true", help="Include hidden files")

parser.add_argument("-1", "--singleColumn", action="store_true", help="List one file per line") 
args = parser.parse_args()

file_paths = args.paths
show_long = args.longList
show_all = args.all
force_single_column = args.singleColumn 

def format_permissions(mode):
    return stat.filemode(mode)

for input_path in file_paths:
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f'No such file or directory: {input_path}')
        
        if os.path.isfile(input_path):
            if show_long:
                file_stat = os.stat(input_path)
                perms = format_permissions(file_stat.st_mode)
                size = str(file_stat.st_size).rjust(6)
                print(f"{perms}  {size}  {input_path}")
            else:
                print(input_path)

        elif os.path.isdir(input_path):
            entries = os.listdir(input_path)
            if not show_all:
                entries = [e for e in entries if not e.startswith(".")]

            # Optional: sort entries for consistent output
            entries.sort()  # (optional for predictable output)

            for entry in entries:
                full_path = os.path.join(input_path, entry)
                entry_stat = os.stat(full_path)
                if show_long:
                    perms = format_permissions(entry_stat.st_mode)
                    size = str(entry_stat.st_size).rjust(6)
                    print(f"{perms}  {size}  {entry}")
                elif force_single_column:
                    print(entry)
                else:
                    print(entry)  

    except Exception as e:
        print(f'Error reading "{input_path}": {e}', file=sys.stderr)
        sys.exit(1)

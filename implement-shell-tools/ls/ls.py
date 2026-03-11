import os
import argparse
import locale


#set locale to the machine default setting
locale.setlocale(locale.LC_ALL, '')


parser = argparse.ArgumentParser(
    prog="ls",
    description="An alternative to the 'ls' command",
)

parser.add_argument("directory", nargs="?", default=".", help="The directory to list (defaults to the current directory)")
parser.add_argument("-1", "--single-column", action="store_true", help="List all files, one per line")
parser.add_argument("-a", "--all", action="store_true", help="Include hidden files (those starting with .) in the listing")

args = parser.parse_args()

# check if path exists 
if not os.path.exists(args.directory):
    print(f"ls: cannot access '${args.directory}': No such file or directory")
    exit(1)

# check if path is a directory
if os.path.isdir(args.directory):
    entries = os.listdir(args.directory)

    # if -a flag set
    if args.all:
        entries.extend(['.', '..'])

    # filter hidden files if -a (all) flag not set
    if not args.all:
        entries = [entry for entry in entries if not entry.startswith(".")]

    # sort the entries using locale-aware comparison
    entries.sort(key =locale.strxfrm)

    # print entries
    if args.single_column:
        for entry in entries:
            print(entry)
    else:
        print("  ".join(entries))
        
import argparse
import os    #interacting with the filesystem (paths, directories)
import sys   #access to system streams (stdout, stderr) and arguments

def parseargs():
    parser = argparse.ArgumentParser(
        prog = "ls",
        description = "ls clone to -1 and -a flags"
    )
    parser.add_argument("-1", dest = "one_per_line", action = "store_true",help = "List one file per line") #dest sets the attribute name in parsed argument.
    parser.add_argument("-a", "--all", action ="store_true",help = "Include directory entries whose names begin with a dot (.)")
    parser.add_argument("dirs", nargs = "*", default = ["."], help = "Directories to list (default is current directory)")
    return parser.parse_args()

def print_directory_entries(path, one_per_line=False, show_all=False):
    try:
        # Retrieve all entries (files and subdirectories) inside the given path
        directory_entries = os.listdir(path)
    except FileNotFoundError:
        # If the directory doesn't exist, print an error to stderr
        print(f"ls: cannot access '{path}': No such file or directory", file=sys.stderr)
        return
    except PermissionError:
        # If the directory exists but we don't have permission, print an error
        print(f"ls: cannot open directory '{path}': Permission denied", file=sys.stderr)
        return

    # By default, ls hides "dotfiles" (names starting with ".").
    # Only include them if the -a flag (show_all=True) is set.
    if show_all:
        directory_entries.extend([".",".."])
    else:
        #Filter out hidden files
        directory_entries = [entry for entry in directory_entries if not entry.startwith(".")]
    #output consistent with the default ls behavior.
    directory_entries.sort()

    if one_per_line:
        # If -1 flag is set, print each entry on its own line
        for entry_name in directory_entries:
            print(entry_name)
    else:
        # Default behavior: print entries space-separated on one line
        print("  ".join(directory_entries))

def main():
    args = parseargs()
    # Loop through each directory provided
    for directory in args.dirs:
        print_directory_entries(
            directory,
            one_per_line = args.one_per_line,
            show_all = args.all
        )
if __name__ == "__main__":
    main()
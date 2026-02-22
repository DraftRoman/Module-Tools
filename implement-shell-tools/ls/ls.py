# This program is a basic version of the 'ls' command in Unix.
# It lists the files and folders in a given directory.
# You can show hidden files with `-a` and print one item per line with `-1`.

import argparse
import os

def setup_arguments():
    # Set up command-line arguments
    parser = argparse.ArgumentParser(
        prog="custom_ls",
        description="Lists contents of a directory"
    )
    # Optional path (defaults is current directory)
    parser.add_argument(
        "path", nargs="?", default=".",
        help="Path to the target directory (defaults to current)"
    )
    # Option to show one entry per line
    parser.add_argument(
        "-1", dest="linewise", action="store_true",
        help="Display one entry per line"
    )
    # Option to include hidden files
    parser.add_argument(
        "-a", dest="include_hidden", action="store_true",
        help="Include hidden files in the output"
    )
    return parser.parse_args()

def list_directory(path, show_hidden, one_per_line):
    try:
        # Try to get the list of items in the directory
        items = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: '{path}' not found.")  # If directory doesn't exist
        return
    except NotADirectoryError:
        print(f"Error: '{path}' is not a directory.")  # If it's not a directory
        return

    # Filter out hidden files unless the user wants them
    entries = [
        entry for entry in sorted(items)
        if show_hidden or not entry.startswith(".")
    ]

    # Print entries one per line or all on one line
    if one_per_line:
        for entry in entries:
            print(entry)
    else:
        print("  ".join(entries))

def main():
    # Get user options and run the directory listing
    args = setup_arguments()
    list_directory(
        path=args.path,
        show_hidden=args.include_hidden,
        one_per_line=args.linewise
    )

# Run the program
if __name__ == "__main__":
    main()

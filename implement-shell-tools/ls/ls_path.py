# Buil-in module to parse command-line arguments and options
import argparse
# For converting the given path to an absolute path
from pathlib import Path
# For colouring terminal output (blue for directories)
from colorama import Fore, Style, init

# Sets up colorama for blue colour for directories
init()

# Function to list directories, files
def list_directory_files(dir_path: Path, display_hidden_files=False, display_one_per_line=False):
    try:
        # Get all entries (files and directories) as Path objects
        entries = list(dir_path.iterdir())
        # A list to store . and ..
        dot_dirs = []
        # If the user set '-a', will store '.', '..'
        if display_hidden_files:
            # Adds "." (current directory) and ".." (parent directory) to the list
            dot_dirs = [Path("."), Path("..")]

        # Filter out hidden files if not showing them
        if not display_hidden_files:
            entries = [e for e in entries if not e.name.startswith(".")]

        # Combine dot_dirs with the visible entries list
        visible_entries = dot_dirs + entries

        # Sort alphabetically lamba function for ignoring "." and case-insensitive
        visible_entries.sort(key=lambda p: p.name.lstrip(".").lower())
        # Create a list for styled directories, files
        styled_entries = []
        
        # For in loop for styling directories 
        for entry in visible_entries:
            # Check for directory
            if entry.is_dir():
                # Apply styles for directory, add to the styled_entries
                styled_entries.append(Fore.BLUE + Style.BRIGHT + entry.name + Style.RESET_ALL)
            else:
                # If file, just add to the list
                styled_entries.append(entry.name)
                
        # If the user set a "-1" flag, print each entry on a new line
        if display_one_per_line:
            print("\n".join(styled_entries))
        # If the user doesn't set a "-1" flag, print all entries on the same line
        else:
            print("  ".join(styled_entries))

    # Handle errors   
    
    # Exception - is the base class for all built-in exceptions
    # error - an exception object
    
    except Exception as error:
        print(f"Error reading directory: {error}")
        
# Setup argument parser. Creates an instance(object) from built-in ArgumentParser class
parser = argparse.ArgumentParser(prog="ls command",
    description="Implement 'ls' command with -1 and -a flags",
    epilog="Now you can see the files in the chosen path"
)
# Define flags and arguments
# Define dest="one_per_line" for "-1", because -1 is not valid Python variable
parser.add_argument("-1", dest="one_per_line", action="store_true", help = "Display each file on a new line")
parser.add_argument("-a", action="store_true", help = "Display all files including hidden files")
# Positional argument. Defaults to . (current directory) if not provided. nargs="?" - optional, takes 0 or 1 value
parser.add_argument("path", nargs="?", default = ".", help = "Specify file path to the list")

# Parse the command-line arguments. args - an instance of the class argparse.Namespace
args = parser.parse_args()

# Get absolute path
absolute_path = Path(args.path).resolve()
list_directory_files(absolute_path, display_hidden_files=args.a, display_one_per_line=args.one_per_line)

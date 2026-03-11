# Buil-in module to parse command-line arguments and options
import argparse
# Finds all file paths matching a pattern
import glob

# Setup argument parser. Creates an instance(object) from built-in ArgumentParser class
parser = argparse.ArgumentParser(
    prog="cat command",
    description="Implement 'cat' command with -n and -b flags",
    epilog="Now you can see the content of files with numbers of lines")

# Define flags and arguments
parser.add_argument("-n", action="store_true", help="Show the content with numbers of each lines")
parser.add_argument("-b", action="store_true", help="Show the content with numbers of each lines which is not empty")
# Add positional argument for one or more file paths (nargs="+")
parser.add_argument("paths", nargs="+", help="Specify file paths, included wildcards")

# Create args - an instance of the class argparse.Namespace
args = parser.parse_args()

# A global variable to keep track of line numbers across all files
line_number = 1

# Function to display content and lines for specific condition which a user provides
def display_file_contents(file_path, display_line_numbers = False, display_not_empty_line_numbers = False):   
    # Make sure that this variable refers to the global line_number to persist across different files
    global line_number
    try:
        # Open file. "r" - read mode. with - ensure the file will be closed after the block of code finishes running.
        with open(file_path, "r", encoding = "utf-8") as file_object:
           # loopp through each line
            for line in file_object:               
                # rstrip("\n") - removes any trailing newline character (\n) from the end of each line
                line_to_print = line
                # if a user set "-b" flag
                if display_not_empty_line_numbers:
                    # Print if there is not empty line after removing any whitespace from the start and end of the line
                    if line.strip():
                        # {line_number:6} - string formatting
                        print(f"{line_number:6}  {line_to_print}", end="")
                        # Increments the line number after printing the line.
                        line_number += 1
                    else:
                        print(line_to_print)
                elif display_line_numbers:
                    # f - f-string, formatted string literal
                    print(f"{line_number:6}  {line_to_print}", end="")
                    line_number += 1
                else:
                    print(line_to_print, end="")
     # Handle errors   
    
    # Exception - is the base class for all built-in exceptions
    # error - an exception object
    except Exception as error:
        print(f"Error reading file {file_path}: {error}")

# Collect all matched files into matched_files list
matched_files = []
# args.paths- is a list of file paths provided by the user
# glob.glob() takes a string path pattern from user, and returns a list of all files that match it.
# Add, using .extend() method, to the matched_files list
for path in args.paths:
    matched_files.extend(glob.glob(path)) 

# print error message if file is not exist
if not matched_files:
    print(f"No files matched the given pattern: {args.paths}") 
    # exit(1) - stop the program with 1 code that indicates the error. exit(0)
    exit(1)

# For in loop to process each file using for in loop
for file_path in matched_files:
    display_file_contents(file_path, display_line_numbers = args.n, display_not_empty_line_numbers = args.b)
    
            
        
        


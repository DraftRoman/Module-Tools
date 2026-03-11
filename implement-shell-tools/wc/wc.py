# Built-in module to parse command-line arguments and options
import argparse
# Finds all file paths matching a pattern
import glob
# Built-in module to provide functions for interacting with the operating system, open, write, manipulate (file size, paths etc.)
import os

# Function to compute line, word, and byte counts. filepath - a string (path to a file)
def wc_counts(filepath):    
    try:
        # Open file. "r" - read mode. with - ensure the file will be closed after the block of code finishes running.
        with open(filepath, "r", encoding="utf-8") as file_object:
            # Read all the entire content and returns it as a string in file_content_string
            file_content_string = file_object.read()            
        # Count the number of newline characters by using .count() method - counts the number of occurrences of the specified substring 
        lines = file_content_string.count("\n")
        # Count the number of words (split by any whitespace by default) using length of the list
        words = len(file_content_string.split())
        # Get the size of the file in bytes. getsize() returns the size of the file in bytes
        byte_size = os.path.getsize(filepath)
        return lines, words, byte_size
    
    # Handle errors   
    
    # Exception - is the base class for all built-in exceptions
    # error - an exception object
    except Exception as error:
        # f - f-string, formatted string literal
        print(f"Error reading file {filepath}: {error}")        
        # return fallback values
        return 0, 0, 0    

# Setup argument parser. Creates an instance(object) from built-in ArgumentParser class
parser = argparse.ArgumentParser(
    prog="wc command",
    description="Implementing 'wc' command (-c, -w, -l flags) functionality in Python",
    epilog="That's how you count the bytes, words, and lines"   
)

# Define flags and arguments
parser.add_argument("-l", action="store_true", help="Count lines")
parser.add_argument("-w", action="store_true", help="Count words")
parser.add_argument("-c", action="store_true", help="Count bytes")
# Add positional argument for one or more file paths (nargs="+")
parser.add_argument("paths", nargs="+", help="File paths (wildcards supported)")

# Parse the command-line arguments. args - an instance of the class argparse.Namespace
args = parser.parse_args()

# If no flags are provided, display all flags
display_all = not (args.l or args.w or args.c)

# Initialisation of count total of lines, words, bytes
total_lines, total_words, total_bytes = 0, 0, 0

# Collect all matched files into matched_files list
matched_files = []
# args.paths- is a list of file paths provided by the user
# glob.glob() takes a string path pattern from user, and returns a list of all files that match it.
# Add, using .extend() method, to the matched_files list
for path in args.paths:
    matched_files.extend(glob.glob(path))
    
# print error message if file does not exist
if not matched_files:
    print(f"No files matched the given pattern: {args.paths}")
    # exit(1) - stop the program with 1 code that indicates the error. exit(0) - indicates the program ran successfully
    exit(1)

# For in loop to process each file using for in loop
for filepath in matched_files:
    # Get counts for the current file
    lines, words, byte_size = wc_counts(filepath)
    
    # Accumulate totals for summary (if multiple files)
    total_lines += lines
    total_words += words
    total_bytes += byte_size
    
    # Format the output line. str() - convert integer to a string, .rjust(7)-  right-aligns the string representation of the number by padding it with spaces to a total length of 7 characters
    # None - don't apply conditionals
    # output - a list with integers of lines, words, bytes and file path
    output = [
        str(lines).rjust(3) if args.l or display_all else None,
        str(words).rjust(3) if args.w or display_all else None,
        str(byte_size).rjust(3) if args.c or display_all else None,
        filepath
    ]    
    # Print the output line (filter out None entries)
    print(" ".join([item for item in output if item is not None]))

# Conditional for multiple files to count and print totals of lines, words, bytes for each file
if len(matched_files) > 1:
    output = [
        str(total_lines).rjust(3) if args.l or display_all else None,
        str(total_words).rjust(3) if args.w or display_all else None,
        str(total_bytes).rjust(3) if args.c or display_all else None,
        "total"
    ]
    print(" ".join([item for item in output if item is not None]))

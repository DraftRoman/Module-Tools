# This program is a simple version of the 'wc' command.
# It counts lines, words, and characters in one or more text files.
# You can choose to count only lines (-l), words (-w), or characters (-c), or show all by default.

import argparse

def setup_arguments():
    # Set up command-line 
    parser = argparse.ArgumentParser(
        prog="wordcount",
        description="A simple wc clone that reads files and displays line, word, and character counts."
    )
    # Add file names (at least one)
    parser.add_argument("files", nargs='+', help="Files to analyze")
    # Optional flags to count lines, words, or characters
    parser.add_argument("-l", "--lines", action="store_true", help="Count lines")
    parser.add_argument("-w", "--words", action="store_true", help="Count words")
    parser.add_argument("-c", "--chars", action="store_true", help="Count characters")
    
    return parser.parse_args()

def read_text_from_file(path):
    # Read the full content of a file
    with open(path, "r") as f:
        return f.read()

def count_lines(text):
    # Count the number of lines
    return len(text.rstrip('\n').split('\n'))

def count_words(text):
    # Count the number of words
    return len(text.split())

def count_characters(text):
    # Count the number of characters
    return len(text)

def analyze_file(path):
    # Analyze a file and return line, word, and character counts
    data = read_text_from_file(path)
    return {
        "lines": count_lines(data),
        "words": count_words(data),
        "chars": count_characters(data)
    }

def show_counts(counts, path, opts):
    # Print the counts for a single file
    if opts.lines:
        print(counts["lines"], path)
    elif opts.words:
        print(counts["words"], path)
    elif opts.chars:
        print(counts["chars"], path)
    else:
        print(counts["lines"], counts["words"], counts["chars"], path)

def show_total(all_counts, opts):
    # Show total counts if more than one file is used
    total = {
        "lines": sum(c["lines"] for c in all_counts),
        "words": sum(c["words"] for c in all_counts),
        "chars": sum(c["chars"] for c in all_counts)
    }
    if opts.lines:
        print(total["lines"], "total")
    elif opts.words:
        print(total["words"], "total")
    elif opts.chars:
        print(total["chars"], "total")
    else:
        print(total["lines"], total["words"], total["chars"], "total")

def main():
    # Main program logic
    options = setup_arguments()  # Get user input
    all_results = []  # Store results for all files

    for file in options.files:
        result = analyze_file(file)  # Analyze each file
        all_results.append(result)
        show_counts(result, file, options)  # Print results for each file

    if len(options.files) > 1:
        show_total(all_results, options)  # Print total if multiple files

# Run the main function
if __name__ == "__main__":
    main()

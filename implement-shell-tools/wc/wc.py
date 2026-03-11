import argparse
import locale


#set locale to the machine default setting
locale.setlocale(locale.LC_ALL, '')

parser = argparse.ArgumentParser(
    prog="wc",
    description="An alternative to the 'wc' command",
)
parser.add_argument("files", nargs="+", help="The file(s) to process")
parser.add_argument("-l", "--lines", action="store_true", help="Print the newline counts")
parser.add_argument("-w", "--words", action="store_true", help="Print the word counts")
parser.add_argument("-c", "--bytes", action="store_true", help="Print the byte counts")

args = parser.parse_args()

# when no specific flags are set
no_flags = not (args.lines or args.words or args.bytes)

totals = {"lines": 0, "words": 0, "bytes": 0}

def calculate_counts(content):
    # returns a count object
    return {
        "lines": content.count('\n') + (1 if content and not content.endswith('\n') else 0), # count lines by '\n'; add 1 if last line has no newline to match real wc command behavior"
        "words": len(content.split()),
        "bytes": len(content.encode('utf-8')),
    }


def print_counts(counts, file):
    parts = []
    # map flag args to the keys in the count object
    flag_arg_to_key = {
        "lines": args.lines,
        "words": args.words,
        "bytes": args.bytes
    }

    PADDING = 3

    for key, flag in flag_arg_to_key.items():
        if no_flags or flag:
            # apply padding only when no_flags is True
            padded_output = f"{counts[key]:>{PADDING}}" if no_flags else str(counts[key])
            parts.append(padded_output)
    parts.append(file)
    print(" ".join(parts))


for file in args.files:
    try: 
        with open(file, "r") as f:
            # read the content and split the lines ready to process as needed
            content = f.read()  
            counts = calculate_counts(content)
        # update totals object with values from count object
        for key in totals:
            totals[key] += counts[key]
        print_counts(counts, file)    
    except FileNotFoundError:
        print(f"wc: {file}: No such file or directory found") 

# Print totals if more than one file
if len(args.files) > 1:
    print_counts(totals, "total")

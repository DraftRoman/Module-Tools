import argparse

parser = argparse.ArgumentParser(prog="wc", description="Count lines, words, and characters")
parser.add_argument("paths", nargs='+', help="Files to count")
parser.add_argument("-l", "--lines", action="store_true")
parser.add_argument("-w", "--words", action="store_true")
parser.add_argument("-c", "--chars", action="store_true")

args = parser.parse_args()

# If no flags are provided, the default behavior is to show all three
show_all = not (args.lines or args.words or args.chars)

total_stats = [0, 0, 0] # lines, words, chars

for path in args.paths:
    with open(path, "r") as f:
        content = f.read()

    stats = [
        len(content.splitlines()), 
        len(content.split()), 
        len(content)
    ]
    
    for i in range(3):
        total_stats[i] += stats[i]

    output = []
    if args.lines or show_all: output.append(f"{stats[0]:8}")
    if args.words or show_all: output.append(f"{stats[1]:8}")
    if args.chars or show_all: output.append(f"{stats[2]:8}")
    
    print(f"{''.join(output)} {path}")

if len(args.paths) > 1:
    total_output = []
    if args.lines or show_all: total_output.append(f"{total_stats[0]:8}")
    if args.words or show_all: total_output.append(f"{total_stats[1]:8}")
    if args.chars or show_all: total_output.append(f"{total_stats[2]:8}")
    
    print(f"{''.join(total_output)} total")
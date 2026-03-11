import argparse
import sys
import glob # to find file paths and match patterns



def parse_args():
    parser = argparse.ArgumentParser(
        prog = "cat",
        description= "copying cat commands behavior with -n and -b flags"
    )
    parser.add_argument("-n", "--number", action="store_true", help="Number all output lines")  #with store true argument behaves like a boolean, flag present returns true, not present = false.
    parser.add_argument("-b", "--number-nonblank", action="store_true", help="Number non-empty output lines")
    parser.add_argument("files", nargs="+", help="Files to read (supports shell globs)") # accepts one or more files names or glob patterns.
    return parser.parse_args()

#Uses glob to expand patterns like *.txt.
def expand_files(patterns):
    expanded = []
    for p in patterns:
        matches = glob.glob(p)
        if matches:
            expanded.extend(sorted(matches))  # predictable order
        else:
            print(f"cat: {p}: No such file", file=sys.stderr) #Prints an error if a pattern matches nothing.
    return expanded

def cat_file(filename, number_all=False, number_nonempty=False):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"cat: {filename}: No such file")
        return
#Applies numbering rules depending on flags.
    line_num = 1
    for line in lines:
        line = line.rstrip('\n')
        if number_all:
            print(f"{line_num:6}  {line}")
            line_num += 1
        elif number_nonempty:
            if line.strip():
                print(f"{line_num:6}  {line}")
                line_num+= 1
            else:
                print(line)
        else:
            print(line)

def main():
    args = parse_args() #return an args obj
    files = expand_files(args.files) #list of filenames or patterns user typed passed to expand_files helper that uses glob module to expand patterns to actual file paths
    if not files:
        sys.exit(1)  #programs exits with status code 1- signals and error if no files were found

#looping through each file path on expanded list
    for file in files: 
        cat_file(file, number_all=args.number, number_nonempty=args.number_nonblank)

if __name__ == "__main__":
    main()
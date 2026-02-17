import argparse
import sys

def cat_file(file_path, number_all_lines, number_non_blank):
    try:
       with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

            for line_num, line in enumerate(lines, start=1):
                prefix = ""

                # -n: number all lines
                if number_all_lines:
                    prefix = f"{line_num:6}\t" # 'line_num:6' means align right

                # -b: number only non-blank lines
                elif number_non_blank and line.strip() != "":
                        prefix = f"{line_num:6}\t"

                print(f"{prefix}{line}", end="")
    except FileNotFoundError:
        print(f"cat: {file_path}: No such file or directory", file=sys.stderr)
    except Exception as e:
        print(f"cat: {file_path}: Error reading file: {e}", file=sys.stderr)


parser = argparse.ArgumentParser(
    prog="cat.py",
    description="Display contents of files with optional line numbering."
)

numbering_group = parser.add_mutually_exclusive_group()

numbering_group.add_argument("-n", action="store_true", help="Number all lines")
numbering_group.add_argument("-b", action="store_true", help="Number non-blank lines")
parser.add_argument("files", nargs="+", help="Files to display")

args = parser.parse_args()

# Check if user used -n or -b
number_all_lines = args.n
number_non_blank = args.b

# Loop through all file paths
for file_path in args.files:
    cat_file(file_path, number_all_lines, number_non_blank)

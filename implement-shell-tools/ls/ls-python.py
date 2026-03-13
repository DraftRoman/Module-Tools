import argparse
import os

def main():
    parser = argparse.ArgumentParser(description=" ls in Python")

    parser.add_argument("path", nargs="?", default=".", help="Directory to list")
    parser.add_argument("-a", action="store_true", help="Show hidden files")
    parser.add_argument("-1", dest="one_per_line", action="store_true",
                        help="List one file per line")

    args = parser.parse_args()

    path = args.path
    show_hidden = args.a
    one_per_line = args.one_per_line

    entries = os.listdir(path)

    entries.sort()

    if not show_hidden:
        entries = [f for f in entries if not f.startswith(".")]
    
    if one_per_line:
        for entry in entries:
            print(entry)
    else:
        print(" ".join(entries))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import sys
import os

def print_file(filename, number_all=False, number_nonempty=False):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"cat: {filename}: No such file")
        return

    counter = 1
    for line in lines:
        line = line.rstrip('\n')
        if number_all:
            print(f"{counter:6}  {line}")
            counter += 1
        elif number_nonempty:
            if line.strip():
                print(f"{counter:6}  {line}")
                counter += 1
            else:
                print(line)
        else:
            print(line)

def main():
    import argparse

    parser = argparse.ArgumentParser(description="A Python implementation of cat")
    parser.add_argument('files', nargs='+', help="Files to print")
    parser.add_argument('-n', '--number-all', action='store_true', help="Number all lines")
    parser.add_argument('-b', '--number-nonempty', action='store_true', help="Number non-empty lines")
    args = parser.parse_args()

    for file in args.files:
        print_file(file, number_all=args.number_all, number_nonempty=args.number_nonempty)

if __name__ == "__main__":
    main()

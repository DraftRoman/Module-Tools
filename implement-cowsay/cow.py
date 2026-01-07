#!/usr/bin/env python3

import cowsay

import argparse

listOfAnimals = cowsay.char_names
# setupparser
parser = argparse.ArgumentParser(description="Make animals say things")
parser.add_argument('message', nargs='+', help='The message to say.')
parser.add_argument('--animal', choices=listOfAnimals, default='cow', help='The animal to be saying things.')

# read user input
args = parser.parse_args()
message_str = ' '.join(args.message)

# print the output
print(cowsay.get_output_string(args.animal, message_str))
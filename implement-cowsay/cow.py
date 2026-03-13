#!/usr/bin/env python3
import cowsay
import argparse

animals = cowsay.char_names
parser = argparse.ArgumentParser(prog="cowsay", description="Make animals say things")
parser.add_argument('message', nargs='+')
parser.add_argument('--animal', choices=animals, default='cow')

args = parser.parse_args()
msg_text = ' '.join(args.message)
print(cowsay.get_output_string(args.animal, msg_text))
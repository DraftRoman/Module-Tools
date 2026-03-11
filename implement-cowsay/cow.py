import argparse
import cowsay
import sys

parser = argparse.ArgumentParser(
                    prog='cowsay',
                    description='Make animals say things')

parser.add_argument("--animal", help="The animal to be saying things.", default='cow')
parser.add_argument("message", nargs="*", help="The message to say.")

args = parser.parse_args()
available_animals = cowsay.char_names

message = ' '.join(args.message) if args.message else 'Hello World !'
animal = args.animal

if animal in available_animals:
    print(cowsay.get_output_string(animal, message))
else:
    print(f"Error: '{animal}' is not a valid animal. Available animals are: {', '.join(available_animals)}")
    sys.exit(1)
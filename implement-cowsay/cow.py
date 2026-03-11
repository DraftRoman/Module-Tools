# To handle command-line arguments
import argparse
# To use cowsay functionality
import cowsay

# Set up the argument parser
parser = argparse.ArgumentParser(prog="cowsay", description="Make animals say things")

# Add agruments to specify animal and message.

# --animal -  option specifies the animal to use.
# type=str - type of argument is string.
# choices=list(cowsay.CHARS.keys()) - limits the animal choices to those available in cowsay.
# default='cow' - If no animal is specified, it will default to 'cow'.
# help="The..." - message will be shown when user type '--help' 
parser.add_argument('--animal', type=str, choices=list(cowsay.CHARS.keys()), default='cow', help="The animal to be saying things.")
# message - The text that the animal will say
# nargs='+' - accept more than 1 word as input
parser.add_argument('message', type=str, nargs='+', help="The message to say.")

# Parse the arguments
args = parser.parse_args()

# Dynamically retrieves a function from the cowsay module based on the user's input.
animal_say_func = getattr(cowsay, args.animal)
# Join words into a string and pass the message to the animal_say_func.
animal_say_func(" ".join(args.message))

import cowsay
import argparse

parser = argparse.ArgumentParser(
    prog = "cowsay shell command",
    description = "cowsay shell command on python Make animals say things"
)
# animals = ["beavis","cheese","cow","daemon","dragon","fox","ghostbusters","kitty","meow","miki","milk","octopus","pig","stegosaurus","stimpy","trex","turkey","turtle","tux"]
animals = cowsay.char_names
parser.add_argument("--animal", choices=animals, default = "cow", help="The animal to be saying things.")
parser.add_argument("message", nargs="+", help="The message to say.")

args = parser.parse_args()

cowsay_function = cowsay.char_funcs[args.animal]
cowsay_function(" ".join(args.message))


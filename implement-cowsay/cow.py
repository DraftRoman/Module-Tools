import cowsay
import argparse

parser = argparse.ArgumentParser(description="Make animals say things")
parser.add_argument("--animal", choices=cowsay.char_names, help="The animal to be saying things", default="cow")
parser.add_argument("message", nargs="+", help="The message to say")

args = parser.parse_args()

char_name = args.animal
message = " ".join(args.message)

cowsay_func = getattr(cowsay, char_name)
cowsay_func(message)

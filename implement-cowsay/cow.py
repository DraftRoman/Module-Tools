import argparse
import cowsay

animals = list(cowsay.char_funcs.keys())

parser = argparse.ArgumentParser(description="implement Cowsay command")
parser.add_argument("text",nargs="+" ,help="Text to be displayed")
parser.add_argument("--animal", help=f"Animal to say the text (choices: {', '.join(animals)})", default="cow",choices=animals)
args = parser.parse_args()

text = " ".join(args.text)
animal = args.animal

cowsay.char_funcs[animal](text)    



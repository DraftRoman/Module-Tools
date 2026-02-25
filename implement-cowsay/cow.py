import cowsay
import argparse



parser = argparse.ArgumentParser(prog="cow.py", description="Make animals say things")
parser.add_argument("--animal", choices=cowsay.char_names, help="The animal is saying somethings", default="cow")
parser.add_argument("message", nargs="+", help="The message to say")

args = parser.parse_args()

char_name = args.animal
message = " ".join(args.message)


print(cowsay.get_output_string(args.animal, message))
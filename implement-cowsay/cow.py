import cowsay
import argparse

parser = argparse.ArgumentParser(
    prog="cowsay",
    description="Simple cowsay clone",
)
parser.add_argument("--animal",choices=cowsay.char_names, help="The animal to be saying things.")

parser.add_argument("message",nargs="+", help="Message to be displayed by the cow")
args = parser.parse_args()


msg=" ".join(args.message)
if args.animal is None:
       print(cowsay.get_output_string("cow", msg))

else:
    print(cowsay.get_output_string(args.animal, msg))
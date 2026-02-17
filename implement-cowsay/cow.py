import cowsay
import argparse

list_of_choices = cowsay.char_names


parser = argparse.ArgumentParser(
    prog="cowsay",
    description="Make animals say things",
)

parser.add_argument(
    "--animal",
    nargs="?",
    default="cow",
    help="The animal to be saying things.",
    choices=list_of_choices,
)
parser.add_argument("message", nargs="*", default="", help="message to say")

args = parser.parse_args()

print(cowsay.get_output_string(str(args.animal), " ".join(args.message)))

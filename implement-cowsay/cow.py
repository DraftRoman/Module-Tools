import cowsay
import argparse

parser = argparse.ArgumentParser(description= "animals talking gibberish")

parser.add_argument(

    "--animal",
    choices=cowsay.char_names,
    help="an animal is talking"
)

parser.add_argument(
    "message",
    nargs="+",
    help="msg to say"
)

args = parser.parse_args()

text = " ".join(args.message)

animal = args.animal or "cow"

output = cowsay.get_output_string(animal, text)
print(output)
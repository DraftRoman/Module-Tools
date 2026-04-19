import cowsay
import argparse

animals = [
    name for name in dir(cowsay)
    if callable(getattr(cowsay, name))
    and not name.startswith("_")
]

parser = argrarse.ArgumentParser()
parser.add_argument(
    "--animal",
    default="cow",
    choices=animals
    help="Choose a cowsay character"
)

parser.add_argument("message", nargs="+")

args = parser.parse_args()

text = " ".join(args.message)

if hasattr(cowsay, args.animal):
    getattr(cowsay, args.animal)(text)
else:
    print(f"Unknown animal: {args.animal}. Available: {dir(cowsay)}")

import cowsay
import argparse

parser = argparse.ArgumentParser(prog="cowsay", description="displays cowsay charactor with given arguments")
parser.add_argument('--animal', choices=cowsay.char_names, default="cow", help= 'please enter a valid animal')
parser.add_argument('message', nargs="+", help= 'please enter a message')
arg = parser.parse_args()

msg = " ".join(arg.message)
animal_func = getattr(cowsay, arg.animal)
print(animal_func(msg))

#!/usr/bin/env python3

import argparse
import cowsay
import inspect
import sys

def get_supported_animals():
    animal_list = []
    for name, func in inspect.getmembers(cowsay, inspect.isfunction):
        if not name.startswith('_') and name not in ['cowsay', 'cowthink']:
            animal_list.append(name)
    return sorted(animal_list)


def main():
    animals = get_supported_animals()

    parser = argparse.ArgumentParser(
        prog='cowsay',
        description='Make animals say things'
    )

    parser.add_argument(
        'message',
        nargs='+',
        help='The message to say.'
    )

    parser.add_argument(
        '--animal',
        choices=animals,
        default='cow',
        help=f'The animal to be saying things.'
    )

    args = parser.parse_args()
    message = ' '.join(args.message)

    # Dynamically call the animal function (like cowsay.turtle("hello"))
    try:
        animal_func = getattr(cowsay, args.animal)
        output = animal_func(message)
        if output is not None:
            print(output)
    except AttributeError:
        print(f"Error: '{args.animal}' is not a valid animal.", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()

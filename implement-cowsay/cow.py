#!/usr/bin/env python3
import argparse
import cowsay


def main():
    # 1. Get supported animals dynamically from the library
    animals = list(cowsay.char_names)

    # 2. Set up the argument parser
    parser = argparse.ArgumentParser(
        description="Make animals say things"
    )

    parser.add_argument(
        "--animal",
        choices=animals,
        default="cow",
        help="The animal to be saying things."
    )

    parser.add_argument(
        "message",
        nargs="+",
        help="The message to say."
    )

    # 3. Parse arguments
    args = parser.parse_args()

    # 4. Combine message words into a single string
    text = " ".join(args.message)

    # 5. Dynamically call the correct animal function
    #    e.g. cowsay.cow(text), cowsay.turtle(text), etc.
    speaker = getattr(cowsay, args.animal)
    print(speaker(text))


if __name__ == "__main__":
    main()

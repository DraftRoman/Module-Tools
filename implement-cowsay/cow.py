import argparse
import cowsay

def main():
    # List of available animals (provided by the package)
    animals = cowsay.char_names

    parser = argparse.ArgumentParser(
        prog="cowsay",
        description="Make animals say things"
    )

    parser.add_argument(
        "message",
        nargs="+",
        help="The message to say."
    )

    parser.add_argument(
        "--animal",
        choices=animals,
        default="cow",
        help="The animal to be saying things."
    )

    args = parser.parse_args()

    message = " ".join(args.message)

    # Dynamically call the function for the chosen animal
    animal_func = getattr(cowsay, args.animal)
    animal_func(message)


if __name__ == "__main__":
    main()

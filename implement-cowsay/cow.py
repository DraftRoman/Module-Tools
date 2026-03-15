import argparse
import cowsay


def main():
    parser = argparse.ArgumentParser(
        description="Make animals say things",
    )
    parser.add_argument(
        "--animal",
        choices=cowsay.char_names,
        default="cow",
        help="The animal you want to speak.",
    )
    parser.add_argument(
        "message",
        nargs="+",
        help="The message to say.",
    )

    args = parser.parse_args()
    print(cowsay.get_output_string(args.animal, " ".join(args.message)))


main()

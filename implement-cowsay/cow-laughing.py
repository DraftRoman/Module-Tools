import argparse
import cowsay


def main():
    animals = cowsay.char_names

    parser = argparse.ArgumentParser(
       description="Make animals saying things."
   )

    parser.add_argument(
        "message",
        nargs="+",
        help="The message to say.",
    )

    parser.add_argument(
        "--animal",
        choices=animals,
        help="The animal to be saying things.",
        default="cow",    
    )

    args = parser.parse_args()
    msg = " ".join(args.message)
    
    output = cowsay.get_output_string(args.animal, msg)
    print(output)


if __name__ == "__main__":
    main()
# --- Exercise ---
# Write a program which:

#   1. Already has a list of Laptops that a library has to lend out.
#   2. Accepts user input to create a new Person - it should use the input function to read a person’s name, age, and preferred operating system.
#   3. Tells the user how many laptops the library has that have that operating system.
#   4. If there is an operating system that has more laptops available, tells the user that if they’re willing to accept that operating system they’re more likely to get a laptop.

# You should convert the age and preferred operating system input from the user into more constrained types as quickly as possible, and should output errors to stderr and terminate the program with a non-zero exit code if the user input bad values.

# --- Solution ---
from dataclasses import dataclass
from enum import Enum
from typing import List
import sys


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    return [
        laptop
        for laptop in laptops
        if laptop.operating_system == person.preferred_operating_system
    ]


def read_person_from_input() -> Person:
    try:
        name = input("Enter name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty")

        age_input = input("Enter age: ").strip()
        age = int(age_input)
        if age < 0:
            raise ValueError("Age must be non-negative")

        os_input = input(
            "Enter preferred operating system (macOS, Arch Linux, Ubuntu): "
        ).strip()

        preferred_os = OperatingSystem(os_input)

        return Person(
            name=name,
            age=age,
            preferred_operating_system=preferred_os,
        )

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


LAPTOPS: List[Laptop] = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Lenovo", model="T14 G6", screen_size_in_inches=14, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="MacBook Air", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=5, manufacturer="Lenovo", model="X1 Carbon", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=6, manufacturer="HP", model="Pavilion", screen_size_in_inches=16, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=7, manufacturer="ASUS", model="ExpertBook B1", screen_size_in_inches=14, operating_system=OperatingSystem.ARCH),
    Laptop(id=8, manufacturer="Apple", model="MacBook Pro", screen_size_in_inches=14, operating_system=OperatingSystem.MACOS),
]


def main() -> None:
    person = read_person_from_input()

    matching_laptops = find_possible_laptops(LAPTOPS, person)
    print(
        f"\nNumber of laptops available with "
        f"{person.preferred_operating_system.value}: "
        f"{len(matching_laptops)}"
    )

    laptops_per_os: dict[OperatingSystem, int] = {}
    for laptop in LAPTOPS:
        laptops_per_os[laptop.operating_system] = (
            laptops_per_os.get(laptop.operating_system, 0) + 1
        )

    most_available_os = max(
        laptops_per_os.items(),
        key=lambda item: item[1],
    )[0]

    if most_available_os != person.preferred_operating_system:
        print(
            f"If you're willing to accept {most_available_os.value}, "
            "you're more likely to get a laptop."
        )


if __name__ == "__main__":
    main()

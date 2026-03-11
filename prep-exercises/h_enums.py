import re
import sys
from dataclasses import dataclass
from enum import Enum
from typing import List
from collections import Counter

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_systems: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

def find_possible_laptops(available_laptops: List[Laptop], current_person: Person) -> List[Laptop]:
    return [
        laptop for laptop in available_laptops
        if laptop.operating_system == current_person.preferred_operating_systems
    ]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="MacBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=5, manufacturer="Apple", model="MacBook Air", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=6, manufacturer="Lenovo", model="ThinkPad", screen_size_in_inches=14, operating_system=OperatingSystem.ARCH),
    Laptop(id=7, manufacturer="Asus", model="ZenBook", screen_size_in_inches=13, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=8, manufacturer="HP", model="Spectre", screen_size_in_inches=14, operating_system=OperatingSystem.MACOS),
    Laptop(id=9, manufacturer="Apple", model="MacBook Pro", screen_size_in_inches=16, operating_system=OperatingSystem.MACOS),
]

# ------------------------
# Exercise 1
# ------------------------
#  Write a program which:
#  - Already has a list of Laptops that a library has to lend out.
#  - Accepts user input to create a new Person - it should use the input function to read a person’s name, age, 
#    and preferred operating system.
#  - Tells the user how many laptops the library has that have that operating system.
#  - If there is an operating system that has more laptops available, tells the user that if they’re willing 
#    to accept that operating system they’re more likely to get a laptop.
#  You should convert the age and preferred operating system input from the user into more constrained types as quickly 
#  as possible, and should output errors to stderr and terminate the program with a non-zero exit code if the
#  user input bad values.

def user_prompt() -> Person:
    try:
        name = (input("Please enter your first name: ")).strip()
        # use 're' import (regular expression) for regex validation for allowed name characters
        if not re.fullmatch(r"[A-Za-z\- ]+", name):
            raise ValueError("Name must contain only alphabetic characters, hyphens, or spaces.")
        
        age = int(input("Please enter your age: "))
        minimum_age = 18
        if age < minimum_age: 
            raise ValueError(f"Age must be {minimum_age} or over.")

        
        # define valid OS options
        valid_os = [os.value for os in OperatingSystem]

        # dynamically display the os options (no need for str type here as input always returns a string)
        preferred_os = input(f"Please enter correct operating system name, either {', '.join(valid_os)}: ").strip()

        # validate the OS
        if preferred_os not in valid_os:
            raise ValueError("Invalid operating system.")
    
        # convert to enum
        preferred_os_enum = OperatingSystem(preferred_os)

        return Person(name=name, age=age, preferred_operating_systems=preferred_os_enum)
 
    # throw an error and exit for invalid age and os input
    except ValueError as error:
        print(f"Invalid input: {error}", file=sys.stderr)
        sys.exit(1)



def main() -> None:

    user_details = user_prompt()

    matching_laptops = find_possible_laptops(laptops, user_details)

    # get the counts of the laptops for an OS e.g. os_counts = {OperatingSystem.MACOS: 4,OperatingSystem.ARCH: 2,OperatingSystem.UBUNTU: 3}
    os_counts: Counter[OperatingSystem] = Counter(laptop.operating_system for laptop in laptops)

    print(f"\n{user_details.name}, there are {len(matching_laptops)} laptops available with your preferred operating system ({user_details.preferred_operating_systems.value}).\n")

    if matching_laptops:
        print("Matching laptops:")
        for laptop in matching_laptops:
            print(f"- {laptop.manufacturer} {laptop.model} ({laptop.screen_size_in_inches}\" screen)")
    else:
        print("No laptops available with your preferred operating system.")

    # get the count of laptops for users preferred OS
    user_os_count = os_counts[user_details.preferred_operating_systems]

    # sort alternative OS so most available OS is listed first
    alternative_os = sorted([(os, count) for os, count in os_counts.items() if count > user_os_count], key=lambda x: x[1], reverse=True)
    
    if alternative_os:
        print("\nHowever, there are more laptops available with the following operating systems:")
        for os, count in alternative_os:
            print(f"- {os.value}: {count} laptops")
        print("\nIf you consider one of these options, you will have a greater chance of getting a laptop.")
    else: 
        print("Your preferred operating system has the most laptops available.")

if __name__ == "__main__":
    main()


# EXERCISE 1: 
# Write a program which:

# Already has a list of Laptops that a library has to lend out.
# Accepts user input to create a new Person - it should use the input function to read a person’s name, age, and preferred operating system.
# Tells the user how many laptops the library has that have that operating system.
# If there is an operating system that has more laptops available, tells the user that if they’re willing to accept that operating system they’re more likely to get a laptop.
# You should convert the age and preferred operating system input from the user into more constrained types as quickly as possible, and should output errors to stderr and terminate the program with a non-zero exit code if the user input bad values.

# SOLUTION:

import sys
from dataclasses import dataclass
from enum import Enum
from typing import List

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

# Predefined laptops
laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

def count_laptops_by_os(laptops: List[Laptop]) -> dict:
    os_count = {os: 0 for os in OperatingSystem}
    for laptop in laptops:
        os_count[laptop.operating_system] += 1
    return os_count

def main():
    # --- Input name ---
    while True:
        name = input("Enter your name: ").strip()
        if name:
            break
        print("Error: Name cannot be empty.", file=sys.stderr)

    # --- Input age ---
    while True:
        age_input = input("Enter your age: ").strip()
        try:
            age = int(age_input)
            if age <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Error: Age must be a positive integer.", file=sys.stderr)

    # --- Input preferred OS ---
    os_values = [os.value for os in OperatingSystem]
    while True:
        print("Choose preferred operating system:")
        for os in OperatingSystem:
            print(f"- {os.value}")
        os_input = input("Enter OS: ").strip()
        if os_input in os_values:
            preferred_os = OperatingSystem(os_input)
            break
        print("Error: Invalid operating system.", file=sys.stderr)

    # --- Create Person ---
    new_person = Person(name=name, age=age, preferred_operating_system=preferred_os)

    # --- Count laptops by OS ---
    os_count = count_laptops_by_os(laptops)

    # --- Show count for user's preferred OS ---
    count_for_user_os = os_count.get(new_person.preferred_operating_system, 0)
    print(f"There are {count_for_user_os} laptops available with {new_person.preferred_operating_system.value}.")

    # --- Find the OS with most laptops ---
    max_os = max(os_count, key=os_count.get)
    max_count = os_count[max_os]

    # Suggest alternative if more laptops are available
    if max_os != new_person.preferred_operating_system and max_count > count_for_user_os:
        print(f"Tip: There are more laptops available with {max_os.value} ({max_count} laptops). "
              f"If you're willing to accept that OS, you're more likely to get a laptop.")

if __name__ == "__main__":
    main()

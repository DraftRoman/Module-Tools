#Exercise: Enumeration in Python
# Write a program which:

# Already has a list of Laptops that a library has to lend out.
# Accepts user input to create a new Person - it should use the input function to read a person’s name, age, and preferred operating system.
# Tells the user how many laptops the library has that have that operating system.
# If there is an operating system that has more laptops available, tells the user that if they’re willing to accept that operating system they’re more likely to get a laptop.
# You should convert the age and preferred operating system input from the user into more constrained types as quickly as possible, and should output errors to stderr and terminate the program with a non-zero exit code if the user input bad values.

#solution:

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

laptops = [
    Laptop(1, "Dell", "XPS", 13, operating_system=OperatingSystem.ARCH),
    Laptop(2, "Dell", "XPS", 15, operating_system=OperatingSystem.UBUNTU),
    Laptop(3, "Dell", "XPS", 15, operating_system=OperatingSystem.UBUNTU),
    Laptop(4, "Apple","macBook", 13, operating_system=OperatingSystem.MACOS),
]  

def convert_age(age_str: str) -> int:
    if not age_str.isdigit():
        print("Error: Age must be a positive integer.", file=sys.stderr)
        sys.exit(1)
    return int(age_str)

def count_laptops_by_os(laptops: List[Laptop]):
    counts ={os_enum: 0 for os_enum in OperatingSystem}
    for laptop in laptops:
        counts[laptop.operating_system] += 1
    return counts   

def main():
    name = input("Enter your name: ").strip()
    age_input = input("Enter your age: ").strip()
    preferred_os_str = input("Enter your preferred operating system (macOS, Arch Linux, Ubuntu): ").strip() 
    age = convert_age(age_input)
    
    try:
        preferred_os = OperatingSystem(preferred_os_str)
    except ValueError:
        print(f"Error: '{preferred_os_str}' is not a valid operating system.", file=sys.stderr)
        sys.exit(1)

    person = Person(name=name, age=age, preferred_operating_system=preferred_os)

    os_counts = count_laptops_by_os(laptops)
    preferred_os_count = os_counts[person.preferred_operating_system]

    print(f"There are {preferred_os_count} laptops available with {person.preferred_operating_system.value}.")

    max_os = max(os_counts, key=os_counts.get)
    best_count = os_counts[max_os]

    if max_os != person.preferred_operating_system and best_count > preferred_os_count:
        print(f"If you're willing to accept {max_os.value}, there are {os_counts[max_os]} laptops available."
              f" you would have more laptop options ({best_count} available).")
if __name__ == "__main__":
    main()  


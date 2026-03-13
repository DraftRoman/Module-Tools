'''
Write a program which:
1.Already has a list of Laptops that a library has to lend out.
2.Accepts user input to create a new Person - it should use the input function to 
read a person's name, age, and preferred operating system.
3.Tells the user how many laptops the library has that have that operating system.
4.If there is an operating system that has more laptops available, tells the user 
that if they're willing to accept that operating system they're more likely to get a laptop.

You should convert the age and preferred operating system input from the user 
into more constrained types as quickly as possible, and should output errors to 
stderr and terminate the program with a non-zero exit code if the user input bad values.
'''

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
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops


people = [
    Person(name="Imran", age=22, preferred_operating_system=OperatingSystem.UBUNTU),
    Person(name="Eliza", age=34, preferred_operating_system=OperatingSystem.ARCH),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

print("Library laptops:") # 1. list of laptops
for laptop in laptops:
    print(f"- ID:{laptop.id} {laptop.operating_system.value} - {laptop.manufacturer} {laptop.model} Size: {laptop.screen_size_in_inches}")

# receiving values from input to create person:
name = input("Enter your name: ")

try:
    age_input = input("Enter your age: ")
    age = int(age_input)
except ValueError:
    print("Error: Age must be a number.", file=sys.stderr)
    sys.exit(1)

print("Choose preferred operating system:")
print("1. macOS")
print("2. Arch Linux")
print("3. Ubuntu")
choice = input(">> ")

os_map = {
    "1": OperatingSystem.MACOS,
    "2": OperatingSystem.ARCH,
    "3": OperatingSystem.UBUNTU,
}

preferred_os = os_map.get(choice)

if preferred_os is None:
    print("Error: Invalid operating system selection.", file=sys.stderr)
    sys.exit(1)

person = Person(name=name, age=age, preferred_operating_system=preferred_os)

print(
    f"\nWelcome {person.name}! "
    f"Age: {person.age}, "
    f"Preferred OS: {person.preferred_operating_system.value}"
)
# counts how many laptops there are with that OS
matches_count = sum(
    1 for laptop in laptops
    if laptop.operating_system == person.preferred_operating_system
)
print(f"There are {matches_count} laptop(s) with {person.preferred_operating_system.value}.")

count_laptops_by_os = {
    os_type: sum(1 for laptop in laptops if laptop.operating_system == os_type)
    for os_type in OperatingSystem
}

best_os = max(count_laptops_by_os, key = count_laptops_by_os.get)
best_os_count = count_laptops_by_os[best_os]

if best_os != person.preferred_operating_system:
    print(
        f"There are more laptops available with {best_os.value} "
        f"({best_os_count} laptops). If you're willing to use that OS, "
        "you're more likely to get a laptop."
    )
else:
    print("Good choice! Your preferred OS  has the highest availability.")


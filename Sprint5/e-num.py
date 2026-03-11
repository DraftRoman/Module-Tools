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
    preferred_os: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

#library of laptops
laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_os:
            possible_laptops.append(laptop)
    return possible_laptops   # returns an array of possible laptops for the person

 #accept userinput 
name = input("Enter your name: ").strip()
age_str = input("Enter your age: ").strip()  #input always returns a str, we need to convert this to an integer
os_str = input("Enter your preferred operating system: ").strip()
# Validate age
try:
    age = int(age_str)
except ValueError:
    print("Error: Age must be a number.", file= sys.stderr)
    sys.exit(1)

# Validate OS
try:
    preferred_os = OperatingSystem(os_str)
except ValueError:
    print("Error: Invalid operating system.", file=sys.stderr)
    sys.exit(1)

#Create a person after validation 
person = Person(name = name, age = age, preferred_os =preferred_os)
#finding laptops for this person 
possible = find_possible_laptops(laptops, person)
print(f"The laptop library  has {len(possible)} with {preferred_os.value}.")

# Start with an empty dictionary
os_counts: dict[OperatingSystem, int] = {}

for laptop in laptops:
    os = laptop.operating_system
    # If we've seen this OS before, add 1, otherwise start at 1
    if os in os_counts:
        os_counts[os] += 1
    else:
        os_counts[os] = 1

best_os = None
best_count = -1

# Loop through each (key, value) pair
for pair in os_counts.items():
    os = pair[0]    # the key (operating system)
    count = pair[1] # the value (number of laptops)

    # Check if this count is bigger than the best so far
    if count > best_count:
        best_os = os
        best_count = count

print("Best OS:", best_os, "with", best_count, "laptops")
if best_os != preferred_os:
    print(f"If you’re willing to accept {best_os.value}, "
          f"you’re more likely to get a laptop since there are {best_count} available.")
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




def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops




laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]




namePerson = input("enter your personal name: ")
while True:
    agePerson = input("Enter your age: ")
    if agePerson.isdigit():
        agePerson = int(agePerson)
        break
    print("Invalid age, please try again.")


print("Available operating systems: MACOS, ARCH, UBUNTU")
while True:
    preferredOS = input("Enter your preferred operating system: ").strip().upper()
    try:
        preferredOS = OperatingSystem[preferredOS]
        break
    except KeyError:
     print("Invalid operating system, please try again.")
    
person=Person(name=namePerson, age=int(agePerson), preferred_operating_system=preferredOS)
possible_laptops = find_possible_laptops(laptops, person)
print(f"Possible laptops for {person.name}: {possible_laptops}")




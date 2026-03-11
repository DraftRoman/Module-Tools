from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Tuple

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_systems: Tuple[OperatingSystem, ...]

@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


# Assign each person the best available laptop according to their preference list
# Minimise sadness locally (not globally optimal, but simple and valid for this exercise)
# If no matching OS is available → they get the “least bad” remaining laptop (sadness = 100)

def sadness(person: Person, laptop: Laptop) -> int:
    # Return sadness score for assigning this laptop to this person
    if laptop.operating_system in person.preferred_operating_systems:
        return person.preferred_operating_systems.index(laptop.operating_system)
    return 100


def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    # Every person must get a laptop; spare laptops are allowed
    if len(people) > len(laptops):
         raise ValueError("Not enough laptops for all people.")


    # Clone list so we can remove laptops as they are assigned
    available_laptops = laptops.copy()

    # Creating an empty dictionary
    # what the dictionary should contain
    allocation: Dict[Person, Laptop] = {}

    # stores the single Laptop object that gives the lowest sadness for that person
    for person in people:
        # Pick the laptop with the minimum sadness for this person
        best_laptop = min(
            available_laptops,    # This is a list of laptops that have not been allocated yet
            key=lambda laptop: sadness(person, laptop)  # calculates how "sad" the person would be if they got that laptop
        )                                               # min() returns the laptop with the smallest sadness value.
        
       # assigns that laptop to the person and removes it from the pool of available laptops
        allocation[person] = best_laptop
        available_laptops.remove(best_laptop)

    return allocation

people = [
    Person(name="Imran", age=22, preferred_operating_systems=(OperatingSystem.UBUNTU, OperatingSystem.ARCH)),
    Person(name="Eliza", age=34, preferred_operating_systems=(OperatingSystem.ARCH, OperatingSystem.UBUNTU)),
    Person(name="Fatma", age=18, preferred_operating_systems=(OperatingSystem.MACOS,)),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.UBUNTU),
]       


if __name__ == "__main__":
    allocation = allocate_laptops(people, laptops)

    print("\nLaptop Allocation Results:\n")
    for person, laptop in allocation.items():
        sad = sadness(person, laptop)
        print(f"{person.name} → Laptop {laptop.id} ({laptop.operating_system.value}) | Sadness = {sad}")


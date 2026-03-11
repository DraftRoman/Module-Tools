#If we define "sadness" as the number of places down in someone's ranking 
#the operating system the ended up with (i.e. if your preferences were 
#[UBUNTU, ARCH, MACOS] and you were allocated a MACOS machine your sadness would be 2), 
#  0       1      2      100
#we want to minimize the total sadness of all people. If we allocate someone a laptop 
#with an operating system not in their preferred list, treat them as having a sadness of 100.

from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Optional


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: List[OperatingSystem]
    assigned_laptop: Optional[int] = None

@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem
    assigned: bool = False

# sadnes calculator
def calculate_sadness(person: Person, laptop: Laptop) -> int:
    if laptop.operating_system in person.preferred_operating_system:
        return person.preferred_operating_system.index(laptop.operating_system)
    return 100

def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    best_allocation: Dict[Person, Laptop] = {}
    min_total_sadness = float("inf")

    def backtrack(person_index: int, used_laptops: set, current_alloc: Dict[Person, Laptop], current_sadness: int):
        nonlocal best_allocation, min_total_sadness

        # If all people assigned
        if person_index == len(people):
            if current_sadness < min_total_sadness:
                min_total_sadness = current_sadness
                best_allocation = current_alloc.copy()
            return

        # stop if worse than best
        if current_sadness >= min_total_sadness:
            return

        person = people[person_index]

        for laptop in laptops:
            if laptop.id not in used_laptops:
                sadness = calculate_sadness(person, laptop)

                used_laptops.add(laptop.id)
                current_alloc[person] = laptop

                backtrack(
                    person_index + 1,
                    used_laptops,
                    current_alloc,
                    current_sadness + sadness
                )

                # Undo choice
                used_laptops.remove(laptop.id)
                del current_alloc[person]

    backtrack(0, set(), {}, 0)
    return best_allocation

people = [
    Person(name="Imran", age=22, preferred_operating_system=[OperatingSystem.UBUNTU,OperatingSystem.ARCH,OperatingSystem.MACOS]),
    Person(name="Eliza", age=34, preferred_operating_system=[OperatingSystem.ARCH]),
    Person(name="Maria", age=38, preferred_operating_system=[OperatingSystem.MACOS,OperatingSystem.ARCH]),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

if __name__ == "__main__":
    allocation = allocate_laptops(people, laptops)
    print("Allocation:", allocation)

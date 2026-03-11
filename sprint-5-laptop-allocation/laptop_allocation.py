from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Optional
import sys

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"
@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: List[OperatingSystem]

# custom hash to hash the immutable version of the list
    def __hash__(self) -> int:
        return hash((self.name, self.age, tuple(self.preferred_operating_system)))
@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

# =====define parse operating system======
def parse_operating_system(raw: str) -> OperatingSystem:
   normalized = raw.strip().lower()

   aliases = {
       "macos": OperatingSystem.MACOS,
       "mac": OperatingSystem.MACOS,
       "arch": OperatingSystem.ARCH,
       "arch linux": OperatingSystem.ARCH,
       "ubuntu": OperatingSystem.UBUNTU,
   }


   if normalized not in aliases:
       valid = ", ".join(sorted(aliases.keys()))
       print(f"Error: invalid operating system. Try one of: {valid}", file=sys.stderr)
       sys.exit(1)

   return aliases[normalized]

# ======= sadness helper ============
def sadness(person: Person, laptop: Laptop) -> int:
    laptop_os = laptop.operating_system
    preferences = person.preferred_operating_system
    if laptop_os not in preferences:
        return 100
    return preferences.index(laptop_os)

# ======= Laptop allocation ============
def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    if len(laptops) < len(people):
        raise ValueError("Not enough laptops to allocate one per person.")

    sorted_people = sorted(people, key=lambda p: len(p.preferred_operating_system))

    remaining_laptops = laptops[:]
    assignment: Dict[Person, Laptop] = {}

    for person in sorted_people:
        best_laptop:Optional[Laptop] = None
        best_score = 10**9

        for laptop in remaining_laptops:
            score = sadness(person, laptop)
            if score < best_score:
                best_score = score
                best_laptop = laptop
                if score == 0:
                    break

        if best_laptop is None:
            raise RuntimeError("Allocation failed unexpectedly.")

        assignment[person] = best_laptop
        remaining_laptops.remove(best_laptop)

    return assignment

# ======define main ================
def main() -> None:
    laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13.0, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15.0, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15.0, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13.0, operating_system=OperatingSystem.MACOS),
]

    people = [
        Person(name="Imran", age=22, preferred_operating_system=[OperatingSystem.UBUNTU, OperatingSystem.ARCH, OperatingSystem.MACOS]),
        Person(name="Eliza", age=34, preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.UBUNTU])
    ]

    allocation = allocate_laptops(people, laptops)

    # Print results
    for person, laptop in allocation.items():
        print(f"{person.name}:  Laptop {laptop.id} ({laptop.operating_system.value}) sadness={sadness(person, laptop)}")

if __name__ == "__main__":
    main()

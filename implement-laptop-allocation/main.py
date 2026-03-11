from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

from scipy.optimize import linear_sum_assignment 



class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    # Sorted in order of preference, most preferred is first.
    preferred_operating_systems: List[OperatingSystem]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def sadness(person: Person, laptop: Laptop) ->int:
        if laptop.operating_system in person.preferred_operating_systems:
             return person.preferred_operating_systems.index(laptop.operating_system)
        return 100


def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
     
     if len(people) != len(laptops):
          raise ValueError("Number of individuals and laptops must be equal")
     
     cost_matrix = [
          [sadness(person, laptop) for laptop in laptops]
          for person in people
     ]

     person_indices, laptop_indices = linear_sum_assignment(cost_matrix)

     return {people[p_idx]: laptops[l_idx]
             for p_idx, l_idx in zip(person_indices, laptop_indices)
             
             }





if __name__ == "__main__":
    people = [
        Person(
            name="Alice",
            age=30,
            preferred_operating_systems=[
                OperatingSystem.MACOS,
                OperatingSystem.UBUNTU,
            ],
        ),
        Person(
            name="Bob",
            age=25,
            preferred_operating_systems=[
                OperatingSystem.UBUNTU,
                OperatingSystem.MACOS,
            ],
        ),
        Person(
            name="Carol",
            age=28,
            preferred_operating_systems=[
                OperatingSystem.ARCH,
                OperatingSystem.MACOS,
            ],
        ),
    ]

    laptops = [
        Laptop(
            id=1,
            manufacturer="Apple",
            model="MacBook Air",
            screen_size_in_inches=13.3,
            operating_system=OperatingSystem.MACOS,
        ),
        Laptop(
            id=2,
            manufacturer="Dell",
            model="XPS",
            screen_size_in_inches=13.0,
            operating_system=OperatingSystem.UBUNTU,
        ),
        Laptop(
            id=3,
            manufacturer="Lenovo",
            model="ThinkPad",
            screen_size_in_inches=14.0,
            operating_system=OperatingSystem.ARCH,
        ),
    ]

    allocation = allocate_laptops(people, laptops)

    for person, laptop in allocation.items():
        print(f"{person.name} → {laptop.model} ({laptop.operating_system.value})")

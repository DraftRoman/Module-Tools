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
    preferred_operating_systems: Tuple[OperatingSystem]


@dataclass(frozen=True)
class Laptop:
    id: str
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


people = [
    Person(
        name="Imran",
        age=22,
        preferred_operating_systems=(OperatingSystem.UBUNTU, OperatingSystem.ARCH),
    ),
    Person(
        name="Eliza",
        age=34,
        preferred_operating_systems=(
            OperatingSystem.ARCH,
            OperatingSystem.MACOS,
            OperatingSystem.UBUNTU,
        ),
    ),
    Person(
        name="Ira",
        age=21,
        preferred_operating_systems=(OperatingSystem.UBUNTU, OperatingSystem.ARCH),
    ),
    Person(
        name="Anna",
        age=34,
        preferred_operating_systems=(OperatingSystem.UBUNTU, OperatingSystem.MACOS),
    ),
    Person(
        name="Nahimn",
        age=42,
        preferred_operating_systems=(OperatingSystem.UBUNTU, OperatingSystem.ARCH),
    ),
]

laptops = [
    Laptop(
        id=1,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.ARCH,
    ),
    Laptop(
        id=2,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=15,
        operating_system=OperatingSystem.UBUNTU,
    ),
    Laptop(
        id=3,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=15,
        operating_system=OperatingSystem.UBUNTU,
    ),
    Laptop(
        id=4,
        manufacturer="Apple",
        model="macBook",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.MACOS,
    ),
]


def allocate_laptops(
    people: List[Person], laptops: List[Laptop]
) -> Dict[Person, Laptop]:
    allocation: Dict[Person, Laptop] = {}
    available_laptops = laptops.copy()
    for person in people:
        best_laptop = None
        big_sadness = 100
        for laptop in available_laptops:
            if laptop.operating_system in person.preferred_operating_systems:
                sadness = person.preferred_operating_systems.index(
                    laptop.operating_system
                )
            else:
                sadness = 100

            if sadness < big_sadness:
                big_sadness = sadness
                best_laptop = laptop

        if best_laptop is not None:
            allocation[person] = best_laptop
            available_laptops.remove(best_laptop)
    return allocation


allocation = allocate_laptops(people, laptops)

for person, laptop in allocation.items():
    print(f"{person.name} - {laptop.id}")

for person in people:
    if person not in allocation:
        print(f"{person.name} did not get laptop")
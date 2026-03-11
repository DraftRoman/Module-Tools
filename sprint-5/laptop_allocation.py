from dataclasses import dataclass
from enum import Enum
from typing import List, Dict
import numpy as np
from scipy.optimize import linear_sum_assignment

unpreferred_OS_penalty = 100

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: tuple

@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    if len(people) != len(laptops):
        raise ValueError("Number of people must match number of laptops")
    
    n = len(people)
    cost_matrix = np.zeros((n, n), dtype=int)

    for i, person in enumerate(people):
        for j, laptop in enumerate(laptops):
            if laptop.operating_system in person.preferred_operating_system:
                cost_matrix[i, j] = person.preferred_operating_system.index(laptop.operating_system)
            else:
                cost_matrix[i, j] = unpreferred_OS_penalty

    person_indices, laptop_indices = linear_sum_assignment(cost_matrix)

    return {
        people[i]: laptops[j] for i, j in zip(person_indices, laptop_indices)
    }
    
laptops = [
    Laptop(1, "Dell", "XPS 13", 13, OperatingSystem.ARCH),
    Laptop(2, "HP", "Spectre 15", 15, OperatingSystem.UBUNTU),
    Laptop(3, "Lenovo", "ThinkPad 14", 14, OperatingSystem.UBUNTU),
    Laptop(4, "Apple", "MacBook Air", 13, OperatingSystem.MACOS),
    Laptop(5, "Apple", "MacBook Pro", 16, OperatingSystem.MACOS),
    Laptop(6, "Dell", "Latitude", 15, OperatingSystem.ARCH),
    Laptop(7, "HP", "EliteBook", 13, OperatingSystem.MACOS),  
    Laptop(8, "Lenovo", "Yoga", 14, OperatingSystem.UBUNTU)
]

people = [
    Person("Alice", 29, (OperatingSystem.UBUNTU, OperatingSystem.MACOS)),
    Person("Bob", 34, (OperatingSystem.ARCH, OperatingSystem.UBUNTU)),
    Person("Charlie", 40, (OperatingSystem.MACOS, OperatingSystem.ARCH)),
    Person("Diana", 25, (OperatingSystem.MACOS,)),
    Person("Ethan", 31, (OperatingSystem.UBUNTU, OperatingSystem.ARCH)),
    Person("Fiona", 27, (OperatingSystem.MACOS, OperatingSystem.UBUNTU)),
    Person("George", 22, (OperatingSystem.ARCH, OperatingSystem.MACOS)),
    Person("Zara", 33, (OperatingSystem.ARCH, OperatingSystem.MACOS))
]

assignment = allocate_laptops(people, laptops)

print("Laptop Assignments:\n")

for person, laptop in assignment.items():
    sadness = (
        person.preferred_operating_system.index(laptop.operating_system)
        if laptop.operating_system in person.preferred_operating_system
        else unpreferred_OS_penalty
    )
    print(f"{person.name} → {laptop.manufacturer} {laptop.model} "
          f"({laptop.operating_system.value}) | Score: {sadness}")

total_sadness = sum(
    person.preferred_operating_system.index(laptop.operating_system)
    if laptop.operating_system in person.preferred_operating_system else unpreferred_OS_penalty
    for person, laptop in assignment.items()
)

print("\nTotal sadness:", total_sadness)

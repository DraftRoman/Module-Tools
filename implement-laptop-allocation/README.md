In the prep, there was an exercise around finding possible laptops for a group of people.

Your exercise is to extend this to actually allocate laptops to the people.

Given these class definitions:

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
    # Sorted in order of preference, most preferred is first.
    preferred_operating_system: List[OperatingSystem]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem
Write a function with this signature:

def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
Every person should be allocated exactly one laptop.

If we define "sadness" as the number of places down in someone's ranking the operating system the ended up with (i.e. if your preferences were [UBUNTU, ARCH, MACOS] and you were allocated a MACOS machine your sadness would be 2), we want to minimise the total sadness of all people. If we allocate someone a laptop with an operating system not in their preferred list, treat them as having a sadness of 100.

Maximum time in hours
3

How to submit
Submit a PR to this repo containing your function (and any supporting code).

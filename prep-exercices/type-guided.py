# EXERCISE 1: 
# Try changing the type annotation of Person.preferred_operating_system from str to List[str].
# Run mypy on the code.
# It tells us different places that our code is now wrong, because we’re passing values of the wrong type.
# We probably also want to rename our field - lists are plural. Rename the field to preferred_operating_systems.
# Run mypy again.
# Fix all of the places that mypy tells you need changing. Make sure the program works as you’d expect.

# When we run mypy, we get the following errors:
# type-guided.py:42: error: Argument "preferred_operating_system" to "Person" has incompatible type "str"; expected "list[str]"  [arg-type]
# type-guided.py:43: error: Argument "preferred_operating_system" to "Person" has incompatible type "str"; expected "list[str]"  [arg-type]

# To solve these errors, I modified the instance to pass a list of strings instead of a single string for the preferred_operating_systems field.
# Also, In order to list all possible laptops for each person, I compared the list of preferred operating systems of each person with the operating system of each laptop.

from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_systems: List[str]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: str


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system in person.preferred_operating_systems:
            possible_laptops.append(laptop)
    return possible_laptops


people = [
    Person(name="Imran", age=22, preferred_operating_systems=["Ubuntu"]),
    Person(name="Eliza", age=34, preferred_operating_systems=["Arch Linux"]),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system="Arch Linux"),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="Ubuntu"),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="ubuntu"),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system="macOS"),
]

for person in people:
    possible_laptops = find_possible_laptops(laptops, person)
    print(f"Possible laptops for {person.name}: {possible_laptops}")
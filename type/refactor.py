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

        for os in person.preferred_operating_systems:
            if laptop.operating_system.lower() == os.lower():
                possible_laptops.append(laptop)
                

    return possible_laptops




people = [
    Person(name="Imran", age=22, preferred_operating_systems=["Ubuntu", "Arch Linux", "macOS", "Windows"]),
    Person(name="Eliza", age=34, preferred_operating_systems=["Arch Linux", "macOS"]),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system="Arch Linux"),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="Ubuntu"),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="ubuntu"),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system="macOS"),
]

for person in people:
    possible_laptops = find_possible_laptops(laptops, person)
    print("-----")
    print(f"Laptops possible for {person.name}:")
    for laptop in possible_laptops:
        print(f"Possible laptop: {laptop.manufacturer} {laptop.id} {laptop.operating_system}")



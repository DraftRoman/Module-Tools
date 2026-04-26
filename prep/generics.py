from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    year_of_birth: int
    children: List["Person"]

fatma = Person(name="Fatma", year_of_birth=2000, children=[])
aisha = Person(name="Aisha", year_of_birth=2010, children=[])

imran = Person(name="Imran", year_of_birth=1989, children=[fatma, aisha])

def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.year_of_birth})")

print_family_tree(imran)
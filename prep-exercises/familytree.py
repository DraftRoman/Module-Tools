from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    children: List["Person"]
    age: int

fatma = Person(name="Fatma", children=[], age=17)
aisha = Person(name="Aisha", children=[], age=25)

imran = Person(name="Imran", children=[fatma, aisha], age=51)

def print_family_tree(person: Person) -> None:
    print(person.name, f"({person.age})")
    for child in person.children:
        print(f"- {child.name} ({child.age})")

# recursion

def print_family_tree_recursion(person: Person, level:str = "¬") -> None:
    print(f"{level} {person.name} ({person.age})")
    for child in person.children:
        print_family_tree_recursion(child, level + "|-")

print_family_tree_recursion(fatma)
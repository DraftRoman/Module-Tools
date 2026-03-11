from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age: int = 0
    children: List["Person"] = None

    def __post_init__(self):
        # Ensure children is always a list
        object.__setattr__(self, "children", self.children or [])

# Example family
fatma = Person(name="Fatma", age=18, children=[])
aisha = Person(name="Aisha", age=24, children=[])
zara = Person(name="Zara", age=2, children=[])  # Fatma's child
fatma = Person(name="Fatma", age=18, children=[zara])  # Fatma now has a child

imran = Person(name="Imran", age=45, children=[fatma, aisha])

def print_family_tree(person: Person, level: int = 0) -> None:
   #  Prints a person's name and age, then recursively prints all descendants
    indent = "  " * level  # 2 spaces per generation
    print(f"{indent}- {person.name} ({person.age})")
    for child in person.children:
        print_family_tree(child, level + 1)

# Print the full family tree
print_family_tree(imran)

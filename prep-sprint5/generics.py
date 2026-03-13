from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    children: List["Person"]

fatma = Person(name="Fatma", age=20, children=[])
aisha = Person(name="Aisha", age=30, children=[])

imran = Person(name="Imran", age=50, children=[fatma, aisha])
maria = Person(name="maria", age=38,children=[fatma])

def print_family_tree(person: Person, level: int = 0) -> None:
    indent = "  " * level
    print(f"{indent}{person.name} ({person.age})")
    
    for child in person.children:
        print_family_tree(child, level + 1)

print_family_tree(maria)

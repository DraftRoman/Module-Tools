# from dataclasses import dataclass
# from typing import List

# @dataclass(frozen=True)
# class Person:
#     name: str
#     children: List["Person"]

# fatma = Person(name="Fatma", children=[])
# aisha = Person(name="Aisha", children=[])

# imran = Person(name="Imran", children=[fatma, aisha])

# def print_family_tree(person: Person) -> None:
#     print(person.name)
#     for child in person.children:
#         print(f"- {child.name} ({child.age})")

# print_family_tree(imran)

# --- Exercise ---
# Fix the above code so that it works. You must not change the print on line 17 - we do want to print the children’s ages. (Feel free to invent the ages of Imran’s children.)

# --- Solution ---
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age:int
    children: List['Person']

fatma = Person(name="Fatma",age=13, children=[])
aisha = Person(name="Aisha",age=6, children=[])

imran = Person(name="Imran",age=42, children=[fatma, aisha])


def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")

print_family_tree(imran)
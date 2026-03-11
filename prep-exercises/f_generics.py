from dataclasses import dataclass
from typing import List, Optional

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


# ------------------------
# Exercise 1
# ------------------------
# Fix the above code so that it works. You must not change the print on line 17 
# - we do want to print the children’s ages. (Feel free to invent the ages of Imran’s children.)

@dataclass(frozen=True)
class Person:
    name: str
    children: List["Person"]
    age: Optional[int] = None  # add the optional import so that age is optional with a default of None
    

fatma = Person(name="Fatma", age=13, children=[])  # order of arguments doesn't matter when named
aisha = Person("Aisha", [], 8)  #however it does if you don't strictly name them

imran = Person(name="Imran", children=[fatma, aisha])

def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")

print_family_tree(imran)
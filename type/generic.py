from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age:int
    children: list['Person']
Aida=Person(name="Aida",age=12, children=[])
Anna=Person(name="Anna",age=12, children=[])

fatma = Person(name="Fatma",age=12, children=[Anna])
aisha = Person(name="Aisha",age=10, children=[Aida])

imran = Person(name="Imran",age=40, children=[fatma, aisha])


def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print_family_tree(child)

print_family_tree(imran)
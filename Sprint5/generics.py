from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age : int
    children: list["Person"] #nside the Person class- the Person-type doesnt exist, so we add "" to person,



Muhib = Person(name="Muhib",age= 7, children=[])
Muiz = Person(name="Muiz",age= 4,children=[])

Sara = Person(name="Sara",age= 31, children=[Muhib, Muiz])

def print_family_tree(person: Person, indent: int = 0) -> None:
    print(" " * indent + f"{person.name} ({person.age})") #indent(int)represents how many spaces to put before the person’s name when printing.
    for child in person.children:
        print_family_tree(child, indent + 2)

print_family_tree(Sara)
#exercise :
# Try changing the type annotation of Person.preferred_operating_system from str to List[str].
# Run mypy on the code.
# It tells us different places that our code is now wrong, because we’re passing values of the wrong type.
# We probably also want to rename our field - lists are plural. Rename the field to preferred_operating_systems.
# Run mypy again.
# Fix all of the places that mypy tells you need changing. Make sure the program works as you’d expect.


    #solution:
    #when I change the str to List[str] and run mypy it shows the following errors:
    # type-guided.py:31: error: "Person" has no attribute "preferred_operating_system"; maybe "preferred_operating_systems"?  [attr-defined]
    # type-guided.py:37: error: Unexpected keyword argument "preferred_operating_system" for "Person"; did you mean "preferred_operating_systems"?  [call-arg]
    # type-guided.py:38: error: Unexpected keyword argument "preferred_operating_system" for "Person"; did you mean "preferred_operating_systems"?             
# then I rename the field to preferred_operating_systems and run mypy again, it shows no errors.
# Here is the corrected code:

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
    Laptop(id=2, manufacturer="Dell", model ="XPS", screen_size_in_inches=15, operating_system="Ubuntu"),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="ubuntu"),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system="macOS"),
]
 

from datetime import date
from dataclasses import dataclass
    
thisYear = date.today().year



@dataclass
class Person:
    name: str
    DoB: int
    preferred_operating_system: str
    
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.DoB = thisYear - age
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self):
        return self.DoB <= thisYear - 18

imran = Person("Imran", 22, "Ubuntu")  # We can call this constructor - @dataclass generated it for us.
print(imran)  

imran2 = Person("Imran", 22, "Ubuntu")
print(imran2)  
print(imran == imran2)  # Prints True because they have the same DoB
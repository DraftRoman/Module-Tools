# class Person:
#     def __init__(self, name: str, age: int, preferred_operating_system: str):
#         self.name = name
#         self.age = age 
#         self.preferred_operating_system = preferred_operating_system

# imran = Person("Imran", 22, "Ubuntu")
# imran2 = Person("Imran", 22, "Ubuntu")

# print(imran == imran2)  # Prints False
# print(imran)  # <__main__.Person object at 0x74b1986e2990>

from dataclasses import dataclass
from datetime import date

# @dataclass(frozen=True)
# class Person:
#     name: str
#     age: int
#     preferred_operating_system: str

# imran = Person("Imran", 22, "Ubuntu")  # We can call this constructor - @dataclass generated it for us.
# print(imran)  # Prints Person(name='Imran', age=22, preferred_operating_system='Ubuntu')

# imran2 = Person("Imran", 22, "Ubuntu")
# print(imran == imran2)  # Prints True


# ------------------------
# Exercise 1
# ------------------------
# Q.Write a Person class using @datatype which uses a datetime.date for date of birth, rather than an int for age.
#   Re-add the is_adult method to it.

@dataclass
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age >= 18
    
imran = Person("Imran", date(2002, 1, 12), "Ubuntu")
print(imran.is_adult())
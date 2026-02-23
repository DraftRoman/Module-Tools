# ✍️exercise
# Write a Person class using @datatype which uses a datetime.date 
# for date of birth, rather than an int for age.

# Re-add the is_adult method to it.

from dataclasses import dataclass
from datetime import date

@dataclass
class Person:
    # def __init__(self, name: str, dob: date, preferred_operating_system: str):
    #     self.name = name
    #     self.dob = dob
    #     self.preferred_operating_system = preferred_operating_system
    name: str
    dob: date
    preferred_operating_system: str    

    def is_adult(self):
        today = date.today()
        age = date.today().year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age >= 18

imran = Person("Imran", date(1988, 10, 10), "Ubuntu")
print(imran.is_adult())
imran = Person("Jay", date(2015, 10, 10), "Ubuntu")
print(imran.is_adult())
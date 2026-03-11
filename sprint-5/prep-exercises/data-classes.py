#Exercise 1:    
# Write a Person class using @datatype which uses a datetime.date for date of birth, rather than an int for age.
# Re-add the is_adult method to it.

#solution:

from dataclasses import dataclass
from datetime import date           
@dataclass(frozen=True) 
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (
            self.date_of_birth.month, self.date_of_birth.day)
            )
        return age >= 18            
imran = Person("Imran", date(2001, 5, 15), "Ubuntu")
print(imran.name)
print(imran.is_adult())
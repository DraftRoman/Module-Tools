'''Write a Person class using @datatype which uses a datetime.date for date of birth, 
rather than an int for age.
Re-add the is_adult method to it.'''
from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today_year = date.today().year
        birth_year = self.date_of_birth.year
        age = today_year - birth_year

        if date.today().month > self.date_of_birth.month:
            return age >= 18
        elif date.today().month == self.date_of_birth.month:
            return date.today().day >= self.date_of_birth.day and age >= 18
        else:
            return age - 1 >= 18

imran = Person("Imran", date(2002, 9, 21), "Ubuntu")
print(imran)
print("Is adult?", imran.is_adult())
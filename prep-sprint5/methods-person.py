
from datetime import date

class Person:
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

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
            

imran = Person("Imran", date(2007,1,19), "Ubuntu")
print(imran.is_adult())
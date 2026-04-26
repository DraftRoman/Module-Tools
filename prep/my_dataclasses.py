from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str
    def is_adult(self) -> bool:
        return self.date_of_birth <= date(2008, 1, 1)  # Anyone born in 2008 or earlier is an adult.
imran = Person("Imran", date(2000, 5, 15), "Ubuntu")
print(imran.name)
print(imran.is_adult())  # Prints True

# Write a Person class using @datatype which uses a datetime.date for date of birth, rather than an int for age.

# Re-add the is_adult method to it.
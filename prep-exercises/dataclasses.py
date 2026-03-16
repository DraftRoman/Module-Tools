# --- Exercise ---
# Write a Person class using @datatype which uses a datetime.date for date of birth, rather than an int for age.

# Re-add the is_adult method to it.

# --- Solution ---
from datetime import date
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month or (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            age -= 1
        return age >= 18   
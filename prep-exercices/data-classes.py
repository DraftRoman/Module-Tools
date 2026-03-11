
# Write a Person class using @datatype which uses a datetime.date for date of birth, rather than an int for age.
# Re-add the is_adult method to it.

from datetime import date
from dataclasses import dataclass

@dataclass (frozen=True)
class Person:
        name: str
        date_of_birth: date
        preferred_operating_system: str

        def is_adult(self) -> bool:
            today = date.today()
            age = today.year - self.date_of_birth.year     
            
                    # Adjust if birthday hasn't happened yet this year
            if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
                age -= 1
            return age >= 18

jesus = Person("Jesus", date(1980, 1, 12), "Ubuntu")
print(jesus.is_adult())


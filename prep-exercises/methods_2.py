# --- Exercise ---
# Change the Person class to take a date of birth (using the standard library’s datetime.date class) and store it in a field instead of age.

# Update the is_adult method to act the same as before.

# --- Solution ---
from datetime import date

class Person:
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

    def is_adult(person: Person) -> bool:
        today = date.today()
        age = today.year - person.date_of_birth.year
        if today.month < person.date_of_birth.month or (today.month == person.date_of_birth.month and today.day < person.date_of_birth.day):
            age -= 1
        return age >= 18   


# exercise
# Change the Person class to take a date of birth 
# (using the standard library’s datetime.date class) and store it in a 
# field instead of age.

# Update the is_adult method to act the same as before.

from datetime import date

class Person:
    def __init__(self, name: str, dob: date, preferred_operating_system: str):
        self.name = name
        self.dob = dob
        self.preferred_operating_system = preferred_operating_system
        

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
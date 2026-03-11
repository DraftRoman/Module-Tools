# EXERCISE 1: Think of the advantages of using methods instead of free functions. Write them down in your notebook
#    - Methods keep data and behavior together
#    - Methods make code easier to read
#    - Methods reduce mistakes
#    - Easier to extend and maintain
#    - Methods support inheritance
#    - Better organization
#    - Better organization
#    - Methods enable polymorphism



# EXERCISE 2: Change the Person class to take a date of birth (using the standard library’s datetime.date class) and store it in a field instead of age.
# Update the is_adult method to act the same as before.


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

imran = Person("Jesus", date(1980, 1, 12), "Ubuntu")
print(imran.is_adult())



from datetime import date


# ------------------------
# Exercise 1
# ------------------------
# Q. Advantages of methods over free functions
# A. Encapsulation - Grouping the data (the attributes) and the behaviour (the  methods) together
#    means that the code is more organised and easier to understand. It also allows you to hide
#    the internal details of how the class works to other parts of the program, so changes
#    to the class can be made without affecting external code. Plus, it prevents
#    accidental changes to the class's data from outside the class.

#    Ease of documentation -  When you use methods, all the actions (functions) related to a specific 
#    thing (like a Person or a String) are grouped inside the class for that thing. This makes it 
#    easier to find and understand what that thing can do because everything is in one place.

#    Inheritance and reusability - methods can be inherited and overridden in subclasses, making them
#    reusable and offering customization.

#    Access to state - Methods can directly access and modify the data (attributes) of an object using 
#    self, which free functions cannot do as they are not tied to any specific object.

#    Polymorphism - Methods support this by allowing you to define methods with the same name in
#    different classes, you call the same methods on different objects but each with behaviour,
#    that is specific to that class.


# ------------------------
# Exercise 2
# ------------------------
# Change the Person class to take a date of birth (using the standard library’s datetime.date class)
# and store it in a field instead of age. Update the is_adult method to act the same as before.

class Person:
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age >= 18

imran = Person("Imran", date(2002, 1, 12), "Ubuntu")
print(imran.is_adult())
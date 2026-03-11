#exercise 1:
# Think of the advantages of using methods instead of free functions. Write them down in your notebook.

#solution:
# 1. Encapsulation: Methods allow for better encapsulation of data and behavior within a class, making it easier to manage and maintain code.
# 2. Code Organization: Methods help organize code by grouping related functionality together within a class, improving readability and structure.
# 3. Inheritance and Polymorphism: Methods can be overridden in subclasses, allowing for polymorphic behavior and code reuse through inheritance.
# 4. Access to Instance Data: Methods have access to the instance's data (attributes), enabling them to operate on the object's state directly.
# 5. Namespace Management: Methods help avoid naming conflicts by being scoped within the class, reducing the likelihood of global namespace pollution.
# 6. Improved Collaboration: In team environments, methods within classes can provide clear interfaces for collaboration, making it easier for multiple developers to work on the same codebase.
# 7. Object-Oriented Design: Methods are a fundamental part of object-oriented programming, promoting principles like encapsulation, abstraction, and modularity.

#exercise 2:
#Change the Person class to take a date of birth (using the standard library’s datetime.date class) and store it in a field instead of age.
#Update the is_adult method to act the same as before.

#solution:

from datetime import date
class Person: 
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system 

    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (
            self.date_of_birth.month, self.date_of_birth.day)
            )
        return age >= 18  
     
imran = Person("Imran", date(2001, 5, 15), "Ubuntu")
print(imran.name)
print(imran.is_adult())
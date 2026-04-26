class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
print(imran.age) # Accessing the "age" attribute of the "imran" object.
print(imran.preferred_operating_system) # Accessing the "preferred_operating_system" attribute of the "imran" object.

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
print(eliza.age) # Accessing the "age" attribute of the "eliza" object.
print(eliza.preferred_operating_system) # Accessing the "preferred_operating_system" attribute of the "eliza" object.

# $ mypy class_and_object.py 
# class_and_object.py:9: error: "Person" has no attribute "address"  [attr-defined]
# class_and_object.py:13: error: "Person" has no attribute "address"  [attr-defined]
# Found 2 errors in 1 file (checked 1 source file)

# after fixing the errors by removing the lines that access the non-existent "address" attribute:
# $ mypy class_and_object.py 
# Success: no issues found in 1 source file

def is_adult(person: Person) -> bool:
    return person.age >= 18

print(f'is Imran an adult: {is_adult(imran)}')

def is_tesla_driver(person: Person) -> bool:
    return person.car == "Tesla" # This will cause an error because the "Person" class does not have a "car" attribute.


def is_tesla_driver_fixed(person: Person) -> bool:
    return hasattr(person, "car") and person.car == "Tesla" # This checks if the "car" attribute exists before trying 
# to access it, preventing an error.
print(f'is Imran a Tesla driver: {is_tesla_driver_fixed(imran)}')
#Ease of documentation - it makes it easier to find all of the things related to a string (or a Person) if they’re attached to that type.
#Encapsulation - if we change the implementation of Person 

class PersonWithDayOfBirth:
    def __init__(self, name: str, day_of_birth: int, preferred_operating_system: str):
        self.name = name
        self.day_of_birth = day_of_birth
        self.preferred_operating_system = preferred_operating_system
    def is_adult(self) -> bool:
        return self.day_of_birth <= 2008 #  Anyone born in 2008 or earlier is an adult.
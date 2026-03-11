class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system



imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
# print(imran.address) # mypy: Person has no attribute address


eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
# print(eliza.address)  # mypy: Person has no attribute address


def is_adult(person: Person) -> bool:
    return person.age >= 18


print(is_adult(imran))


# ------------------------
# Exercise 1
# ------------------------
# Write a new function in the file that accepts a Person as a parameter and tries to access 
# a property that doesn’t exist. Run it through mypy and check that it does report an error.

def is_located_in(person: Person) -> bool:
    return person.is_located_in == "Manchester"

print(is_located_in(eliza))  # prints: AttributeError: 'Person' object has no attribute 'is_located_in'


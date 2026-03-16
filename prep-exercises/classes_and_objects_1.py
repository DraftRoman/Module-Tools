
# class Person:
#     def __init__(self, name: str, age: int, preferred_operating_system: str):
#         self.name = name
#         self.age = age
#         self.preferred_operating_system = preferred_operating_system

# imran = Person("Imran", 22, "Ubuntu")
# print(imran.name)
# print(imran.address)

# eliza = Person("Eliza", 34, "Arch Linux")
# print(eliza.name)
# print(eliza.address)

# --- Exercise ---
# Save the above code to a file, and run it through mypy.

# Read the error, and make sure you understand what it’s telling you.

# --- Solution ---
# The error reads as follows: "Person" has no attribute "address"
# This error occurs because we are trying to access an attribute "address" on the Person class, which has not been defined in the class constructor.
# To fix this error, we can either remove the lines that attempt to access the "address" attribute, or we can add an "address" attribute to the Person class constructor.
# self.address = "Unknown" 
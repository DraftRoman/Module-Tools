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

#exercise 1:
#Read the error, and make sure you understand what it’s telling you.

#solution:
# The error message indicates that the Person class does not have an attribute named "address".
# This means that when the code tries to access eliza.address and imran.address, it fails because the address attribute was never defined in the Person class.
    # class-and-objects.py:9: error: "Person" has no attribute "address"  [attr-defined]
    # class-and-objects.py:13: error: "Person" has no attribute "address"  [attr-defined]
    # Found 2 errors in 1 file (checked 1 source file)

#exercise 2:
# Add the is_adult code to the file you saved earlier.
# Run it through mypy - notice that no errors are reported - mypy understands that Person has a property named age so is happy with the function.
# Write a new function in the file that accepts a Person as a parameter and tries to access a property that doesn’t exist. Run it through mypy and check that it does report an error.

#solution:

class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system    

def is_adult(person: Person) -> bool:
    return person.age >= 18

def get_favorite_color(person: Person) -> str:
    return person.favorite_color  

# When I run mypy on this code, it shows an error related to the get_favorite_color function.
    # class-and-objects.py:42: error: Returning Any from function declared to return "str"  [no-any-return]
    # class-and-objects.py:42: error: "Person" has no attribute "favorite_color"  [attr-defined]
    # Found 2 errors in 1 file (checked 1 source file)
# The error message indicates that the Person class does not have an attribute named "favorite_color".
# This means that when the code tries to access person.favorite_color, it fails because the favorite_color attribute was never defined in the Person class.
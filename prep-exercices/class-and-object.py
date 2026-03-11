#Read the error, and make sure you understand what it’s telling you.



class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system



imran = Person("Imran", 22, "Ubuntu")
print(imran.name)


eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)

def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(imran))


def address(person: Person) -> str:
    return person.address


#EXERCISE 1:
#Add the is_adult code to the file you saved earlier.
#Run it through mypy - notice that no errors are reported - mypy understands that Person has a property named age so is happy with the function.
# Write a new function in the file that accepts a Person as a parameter and tries to access a property that doesn’t exist. Run it through mypy and check that it does report an error.

# SOLUTION:
# After run class-and-object.py, I get the following mypy errors:
# class-and-object.py:12: error: "Person" has no attribute "address"
# It indicates that the Person class does not have an attribute named address.

#EXERCISE 2:
# Add the is_adult code to the file you saved earlier
# Run it through mypy - notice that no errors are reported - mypy understands that Person has a property named age so is happy with the function.

# Write a new function in the file that accepts a Person as a parameter and tries to access a property that doesn’t exist. Run it through mypy and check that it does report an error.
# When running mypy, I get the following error:
# Class-and-object.py:27: error: "Person" has no attribute "address"  [attr-defined]
# Found 1 error in 1 file (checked 1 source file)
# This error indicates that the Person class does not have an attribute named address.

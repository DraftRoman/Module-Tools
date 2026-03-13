'''
Run it through mypy - notice that no errors are reported - mypy understands 
that Person has a property named age so is happy with the function.
Write a new function in the file that accepts a Person as a parameter 
and tries to access a property that doesn't exist. Run it through mypy 
and check that it does report an error.
'''

class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
#print(imran.address)

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
#print(eliza.address)

def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(imran))

''' adding the function:'''
def read_genre(person: Person) -> str:
    if person.genre == "M":
        return "Male"
    else:
        return "Female"

''' returns:
cyf@cyfs-MacBook-Pro prep-sprint5 % mypy class-object-person.py   
class-object-person.py:29: error: "Person" has no attribute "genre"  [attr-defined]
Found 1 error in 1 file (checked 1 source file)

'''

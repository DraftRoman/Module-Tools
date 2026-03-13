class Person:
    def __init__(self, name: str, age: int, address: str, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.address =address
        self.preferred_operating_system = preferred_operating_system

def is_adult(person: Person) -> bool:
    return person.age >= 18

# def get_phone(person: Person) -> str:
#     return person.phone_number

imran = Person("Imran", 22,"Shiraz", "Ubuntu")
print(imran.name)
print(imran.address)

aida = Person("Aida", 34, "Tehran", "Arch Linux")
print(aida.name)
print(aida.address)
print(is_adult(imran))




# def get_phone(person: Person) -> str:
#     return person.phone_number
#
# print(get_phone(aida))
# Person.py:12: error: "Person" has no attribute "phone_number"  [attr-defined]
# Found 1 error in 1 file (checked 1 source file)
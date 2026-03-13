from datetime import date
thisYear = date.today().year


class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = thisYear - age
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self):
        return self.age <= thisYear - 18

imran = Person("Imran", 4, "Ubuntu")
print(imran.is_adult())

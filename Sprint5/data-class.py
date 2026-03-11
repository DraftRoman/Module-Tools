from datetime import date
from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    birth_day: date
    preferred_operating_system: str

    def age(self)-> int:   #returns age in years
        today = date.today()
        years = today.year - self.birth_day.year
        if(today.month, today.day) < (self.birth_day.month, self.birth_day.day):
            years -= 1
        return years

    def is_adult(self):
        return self.age() >= 18
    

p1 = Person("Sara", date(1996, 10, 28), "macOS")
print(p1)  

p2 = Person("Sara", date(1996, 10, 28), "macOS")
print(p1 == p2)  
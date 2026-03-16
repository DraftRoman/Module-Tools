from datetime import date
from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
        name: str
        preferred_operating_system: str
        birth_date: date

        def is_adult(self) -> bool:
            today = date.today()
            age = today.year - self.birth_date.year

            if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
                age -=1
                
            return age >= 18

imran = Person("Imran", "Ubuntu", date(2000, 9, 12))

print(imran.is_adult())




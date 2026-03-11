from datetime import date
class Person:
    def __init__(self, name: str, birth_day: date):
        self.name = name
        self.birth_day = birth_day

    def age(self)-> int:   #returns age in years
        today = date.today()
        years = today.year - self.birth_day.year
        if(today.month, today.day) < (self.birth_day.month, self.birth_day.day):
            years -= 1
        return years

    def is_adult(self):
        return self.age() >= 18
    
    def __str__(self) -> str:
        return f"{self.name}, born {self.birth_day}, age {self.age()}"

p1 = Person("Sara", date(1996, 10, 28))
print(p1.is_adult())   # True

p2 = Person("Muhib", date(2018, 6, 22))
print(p2.is_adult())   # False
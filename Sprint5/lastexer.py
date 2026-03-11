class Parent:
    """Represents a person with a first and last name."""
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        """Return the full name as 'First Last'."""
        return f"{self.first_name} {self.last_name}"


class Child(Parent):   
    """Represents a person who can change last names, tracking previous ones."""
    def __init__(self, first_name: str, last_name: str):
        """Initialize a Child with a first and last name, plus a list of previous last names."""
        super().__init__(first_name, last_name) 
        self.previous_last_names: list[str] = []  

    def change_last_name(self, last_name) -> None:
        """Change the last name and record the previous one."""
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        """Return the full name, with suffix showing original last name if changed."""
        suffix = ""
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"

person1 = Child("Elizaveta", "Alekseeva")
print(person1.get_name())
print(person1.get_full_name())
person1.change_last_name("Tyurina")
print(person1.get_name())
print(person1.get_full_name())

person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name())

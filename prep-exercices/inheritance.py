
#EXERCISE 1:: 

#Play computer with this code. Predict what you expect each line will do.
#Then run the code and check your predictions. (If any lines cause errors, you may need to comment them out to check later lines).

#SOLUTION:

# The first four prints will work fine, as the Child class inherits from the Parent class and has access to its methods.
# The last four prints will get error because the Parent class does not have the methods get_full_name and change_last_name defined.
# Fix the code we can comment out the last four lines or we can add the methods to the Parent class.

class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names = []

    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
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

"""
person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name())
print(person2.get_full_name())
person2.change_last_name("Tyurina")
print(person2.get_name())
print(person2.get_full_name())
"""
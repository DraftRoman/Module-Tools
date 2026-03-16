# --- Exercise ---
# Play computer with this code. Predict what you expect each line will do. Then run the code and check your predictions. (If any lines cause errors, you may need to comment them out to check later lines).

# class Parent:
#     def __init__(self, first_name: str, last_name: str):
#         self.first_name = first_name
#         self.last_name = last_name

#     def get_name(self) -> str:
#         return f"{self.first_name} {self.last_name}"


# class Child(Parent):
#     def __init__(self, first_name: str, last_name: str):
#         super().__init__(first_name, last_name)
#         self.previous_last_names = []

#     def change_last_name(self, last_name) -> None:
#         self.previous_last_names.append(self.last_name)
#         self.last_name = last_name

#     def get_full_name(self) -> str:
#         suffix = ""
#         if len(self.previous_last_names) > 0:
#             suffix = f" (née {self.previous_last_names[0]})"
#         return f"{self.first_name} {self.last_name}{suffix}"

# person1 = Child("Elizaveta", "Alekseeva")
# print(person1.get_name())
# print(person1.get_full_name())
# person1.change_last_name("Tyurina")
# print(person1.get_name())
# print(person1.get_full_name())

# person2 = Parent("Elizaveta", "Alekseeva")
# print(person2.get_name())
# print(person2.get_full_name())
# person2.change_last_name("Tyurina")
# print(person2.get_name())
# print(person2.get_full_name())

# --- Solution ---

# This defines a class called "Parent" with an initializer that sets the first and last name, and a method to get the full name.
class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

# This defines a class called "Child" that inherits from "Parent". It has an initializer that calls the parent's initializer and adds a list that can track previous last names. It also has methods to change the last name and get the full name with any previous last names included.
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

person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name())
print(person2.get_full_name()) # This line will cause an error because the Parent class does not have a get_full_name method.
person2.change_last_name("Tyurina") # This line will cause an error because the Parent class does not have a change_last_name method.
print(person2.get_name())
print(person2.get_full_name()) # This line will cause an error because the Parent class does not have a get_full_name method.

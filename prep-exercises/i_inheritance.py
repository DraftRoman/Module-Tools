class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names: list[str] = []

    def change_last_name(self, last_name: str) -> None:
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
print(person2.get_full_name())
person2.change_last_name("Tyurina")
print(person2.get_name())
print(person2.get_full_name())


# ------------------------
# Exercise 1
# ------------------------
# Play computer with this code. Predict what you expect each line will do. Then run the code and check your predictions. (
# If any lines cause errors, you may need to comment them out to check later lines).

# Line 1: Create the class Parent
# Line 2: Define the constructor method (__init__) that takes self, a first_name value with a type of str, and last_name value with a type of str
# Line 3: Creates the first_name field of the object
# Line 4: Creates the last_name field of the object
# Line 6: Define a get_name method that returns a string
# Line 7: Returns a formatted string of the object's first_name and last_name
# Line 10: Create the subclass Child (inherits from the Parent class)
# Line 11: Define the Child class constructor method and pass in the same arguments of a first_name with a type of str, and last_name with a type of str
# Line 12: Call super() to run the Parent constructor method and set up first_name and last_name
# Line 13: Creates a previous_last_names field (which is unique to the Child and not seen in the Parent class) and sets it to an empty list
# Line 15: Define a change_last_name method that takes a new last_name of type str and doesn't return anything as annotated by the type None
# Line 16: Uses the append method to append the current last_name value to the previous_last_names list
# Line 17: Update the object's last_name field with the new last_name value that was passed in
# Line 19: Define a get_full_name method that returns a string type
# Line 20: Creates a local variable called suffix and sets it to an empty string value
# Line 21: Checks if previous_last_names list has any items (names) by checking the length (checks if it is not empty (i.e. greater than 0))
# Line 22: If it does set the suffix variable to a formatted string that has the word 'née' first then the original last_name value of the previous last name (at the first position in the previous_last_name list)
# Line 23: Returns and formatted string of the Child object's first_name and last_name and adds the suffix at the end

# For person1:  I predict that we will see "Elizaveta Alekseeva" as the first print output for get.name()
#               For get_full_name I predict we will see just "Elizaveta Alekseeva" as there has been no other last names passed to the Child as yet
#               Once change_last_name has been passed a new name, I expect to see "Elizaveta Tyurina"
#               For get_full_name I predict we will see "Elizaveta Tyurina (née Alekseeva)"

# For person2:  I predict that we will see "Elizaveta Alekseeva" for the get.name()
#               I imagine there will be an error for print(person2.get_full_name()) because the Parent does not have a get_full_name method
#               I predict it will fail for person2.change_last_name("Tyurina") for the same reason as the object is a parent object that has no change_last_name method
#               By commenting out the previous 2 lines of code ,the next get.name() will repeat the first print output
#               The final get_full_name output will fail again as before because this method doesn't exist in the Parent class.

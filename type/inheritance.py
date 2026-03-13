from typing import Iterable, Optional

class ImmutableNumberList:
    def __init__(self, elements: Iterable[int]):
        self.elements = [element for element in elements]

    def first(self) -> Optional[int]:
        if not self.elements:
            return None
        return self.elements[0]

    def last(self) -> Optional[int]:
        if not self.elements:
            return None
        return self.elements[-1]

    def length(self) -> int:
        return len(self.elements)
    
    def largest(self) -> Optional[int]:
        if not self.elements:
            return None
        largest = self.elements[0]
        for element in self.elements:
            if element > largest:
                largest = element
        return largest


class SortedImmutableNumberList(ImmutableNumberList):
    def __init__(self, elements: Iterable[int]):
        super().__init__(sorted(elements))

    def largest(self) -> Optional[int]:
        return self.last()

    def max_gap_between_values(self) -> Optional[int]:
        if not self.elements:
            return None
        previous_element = None
        max_gap = -1
        for element in self.elements:
            if previous_element is not None:
                gap = element - previous_element
                if gap > max_gap:
                    max_gap = gap
            previous_element = element
        return max_gap


values = SortedImmutableNumberList([1, 20, 7, 13, 4])
print(values.largest())
print(values.max_gap_between_values())

unsorted_values = ImmutableNumberList([1, 19, 7, 13, 4])
print(unsorted_values.largest())



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

person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name())
print(person2.get_name())

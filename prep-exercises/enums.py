from dataclasses import dataclass
from enum import Enum
from typing import List, Dict





class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name:  str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def count_laptops(laptops: List[Laptop]) -> Dict[OperatingSystem, int]:
    number_eachOS_laptops: Dict[OperatingSystem, int] = {
        OperatingSystem.MACOS: 0,
        OperatingSystem.ARCH: 0,
        OperatingSystem.UBUNTU: 0}
    for laptop in laptops:
        number_eachOS_laptops[laptop.operating_system] +=1
    return number_eachOS_laptops


def count_possible_laptops(laptops: List[Laptop], person: Person) -> int:
    possible_laptops: List[Laptop] =[]
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    number_possible_laptops = len(possible_laptops)
    return number_possible_laptops

def chose_alternative_laptops(laptops: List[Laptop], person: Person) -> Dict[OperatingSystem, int]:
    number_possible_laptops = count_possible_laptops(laptops, person)
    number_eachOS_laptops = count_laptops(laptops)
    preferred_os = person.preferred_operating_system
    alternative_laptops: Dict[OperatingSystem, int] = {}
    for eachOS, count in number_eachOS_laptops.items():
        if eachOS == preferred_os:
            continue
        if count > number_possible_laptops:
            alternative_laptops[eachOS] = count
    if len(alternative_laptops) != 0:
        print("There is an operating system that has more laptops available.If you’re willing to accept them, there is a list:")
        list_os = []
        for os, count in alternative_laptops.items():
            list_os.append(f"{os.value}: {count}")
        print(" ,".join(list_os))
        return alternative_laptops
    else:
        print("There is not an operating system that has more laptops available.")
        return alternative_laptops

while True:
    user_name = input("Type your name: ").strip()
    if len(user_name) < 3:
        print(f"Error, {user_name} is not valid. Try again, length should be more than 3 characters.")
        continue
    break

while True:
    user_age = input("Type your age: ").strip()
    try:
        user_age_int = int(user_age)
        if user_age_int < 18:
            raise ValueError
        break
    except ValueError:
        print("Invalid age, try again! Borrowing allowed from 18 years old.")

available_os = [os.value for os in OperatingSystem]
print("Available OSs are: ", ",".join(available_os))
while True:
    user_operating_system = input("Type operating system: ").strip()
    try:
        if user_operating_system not in available_os:
            raise ValueError
        break
    except ValueError:
        print(f"Error, {user_operating_system} is not in available list\n"
    f"Available OSs are: {','.join(available_os)}. Try again!.", file=sys.stderr)


preferred_operating_system = OperatingSystem(user_operating_system)

user = Person(name=user_name, age=user_age_int, preferred_operating_system=preferred_operating_system)


laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

possible_laptops = count_possible_laptops(laptops, user)
print(f"Possible laptops for {user_name}: {possible_laptops}")
alternative_laptops = chose_alternative_laptops(laptops, user)

import re
import sys
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Tuple

class OperatingSystem(Enum):
    """enumeration of available operating systems."""
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    """represents a person with a name, age, and their OS preferences."""
    name: str
    age: int
    # listed in order of preference
    preferred_operating_systems: Tuple[OperatingSystem, ...]


@dataclass(frozen=True)
class Laptop:
    """represents a laptop with specifications and an operating system."""
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

# In the prep, there was an exercise around finding possible laptops for a group of people.

# Your exercise is to extend this to actually allocate laptops to the people.
# Every person should be allocated exactly one laptop.

# If we define “sadness” as the number of places down in someone’s ranking the operating system the ended
# up with (i.e. if your preferences were [UBUNTU, ARCH, MACOS] and you were allocated a MACOS 
# machine your sadness would be 2), we want to minimise the total sadness of all people. 
# If we allocate someone a laptop with an operating system not in their preferred list, 
# treat them as having a sadness of 100.

laptops_list: List[Laptop] = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="MacBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=5, manufacturer="Apple", model="MacBook Air", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=6, manufacturer="HP", model="Spectre", screen_size_in_inches=14, operating_system=OperatingSystem.MACOS),
]

people: List[Person] = [
    Person(name="Imran", age=18, preferred_operating_systems=[OperatingSystem.UBUNTU, OperatingSystem.ARCH]),
    Person(name="Eliza", age=34, preferred_operating_systems=[OperatingSystem.ARCH, OperatingSystem.MACOS]),
    Person(name="Luke", age=26, preferred_operating_systems=[OperatingSystem.MACOS, OperatingSystem.UBUNTU, OperatingSystem.ARCH]),
    Person(name="Abby", age=30, preferred_operating_systems=[OperatingSystem.MACOS]),
    Person(name="Ger", age=51, preferred_operating_systems=[OperatingSystem.UBUNTU, OperatingSystem.MACOS]),
]


# updated user prompt to include order of preference in selecting OS
def user_prompt() -> Person:
    """
    prompt the user to input their details and preferred operating systems
    """
    try:
        # strip() whitespace before processing (no need for str type here as input always returns a string)
        # use 're' import (regular expression) for regex validation for allowed name characters
        name = input("Please enter your first name: ").strip()
        if not re.fullmatch(r"[A-Za-z\- ]+", name):
            raise ValueError("Name must contain only alphabetic characters, hyphens, or spaces.")
        

        # strip() before converting to integer
        age = int(input("Please enter your age: ").strip())
        minimum_age = 18
        if age < minimum_age: 
            raise ValueError("Age must be {minimum_age} or over.")


        # define valid OS options
        valid_os = [os.value for os in OperatingSystem]

        # prompt the user to enter OS preferences in order of preference (no need for str type here)
        preferred_os = input(f"Please enter your preferred operating systems in order of preference, separated by commas (e.g., {', '.join(valid_os)}): ").strip()

        # split and validate the OS
        preferred_os_list = [os.strip() for os in preferred_os.split(",") if os.strip()]
        if not preferred_os_list:
            raise ValueError("You must enter at least one operating system.")

        preferred_os_enum = []
        for os_name in preferred_os_list:
            if os_name not in valid_os:
                raise ValueError(f"Invalid operating system: {os_name}")
            # convert to enum
            preferred_os_enum.append(OperatingSystem(os_name))

        return Person(name=name, age=age, preferred_operating_systems=tuple(preferred_os_enum))

    # throw an error and exit for invalid age and os input
    except ValueError as error:
        print(f"Invalid input: {error}", file=sys.stderr)


def sadness_score(person: Person, laptop: Laptop) -> int:
    """
    calculate the sadness score for a person based on the allocated laptop.
    """
    if laptop.operating_system in person.preferred_operating_systems:
        return person.preferred_operating_systems.index(laptop.operating_system)
    return 100

def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    """
    allocate laptops to people to minimize total sadness.
    """
    allocated_laptops : Dict[str, Laptop ]= {}

    # create a shallow copy of the laptops list sorted by id
    available_laptops = sorted(laptops, key=lambda l: l.id)
    
    # sort people by length of their preferences first (avoids a score of 100 if possible)
    sorted_people = sorted(people, key=lambda p: len(p.preferred_operating_systems))

    for person in sorted_people:
        # ensure available_laptops is not empty before calling min
        if not available_laptops:
            raise ValueError("No laptops available to allocate.")

        # use min() to find the laptop that minimizes their 'sadness score'
        # lambda function is scoring the person's preferences by calculating the 'sadness score' for each laptop based on the index position
        best_laptop = min(available_laptops, key=lambda laptop: sadness_score(person, laptop))
        allocated_laptops[person.name] = best_laptop
        available_laptops.remove(best_laptop)
 

    if len(allocated_laptops) != len(people):
        raise ValueError("Not enough laptops to allocate one to each person.")

    return allocated_laptops


def main():
    """
    allocate laptops and display results
    """
    try:
        # prompt the user for their details and add them to the people list
        new_person = user_prompt()
        people.append(new_person)
        
        # allocate laptops and print the results
        allocation = allocate_laptops(people, laptops_list)

        for name, laptop in allocation.items():
            person = next(person for person in people if person.name == name)
            person_sadness_score = sadness_score(person, laptop)
            print(f"{name} was allocated {laptop.manufacturer} {laptop.model} with {laptop.operating_system.value} (Score: {person_sadness_score})")

    except Exception as error:
        print(f"An error occurred: {error}", file=sys.stderr)

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
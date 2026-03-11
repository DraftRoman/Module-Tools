from dataclasses import dataclass
from enum import Enum
from typing import Dict, List
import numpy as np  #to build and mnaiplate our sadness grid
from scipy.optimize import linear_sum_assignment #to find optimal laptop allocaation to minimize sadness across all users

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    # Sorted in order of preference, most preferred is first.
    preferred_operating_systems: tuple[OperatingSystem]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

#library of laptops
laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=5, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=6, manufacturer="Dell", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=7, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=8, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]
# Preset dataset of people
people = [
    Person(name="Sara", age=31, preferred_operating_systems=(OperatingSystem.ARCH,OperatingSystem.UBUNTU)),
    Person(name="Shabs", age=40, preferred_operating_systems=(OperatingSystem.ARCH,OperatingSystem.MACOS,OperatingSystem.UBUNTU)),
    Person(name="Jawad", age= 36, preferred_operating_systems=(OperatingSystem.MACOS,OperatingSystem.UBUNTU,OperatingSystem.ARCH)),    
    Person(name="Mike", age=35, preferred_operating_systems=(OperatingSystem.MACOS,OperatingSystem.ARCH)),
    Person(name="Mawra", age=28, preferred_operating_systems=(OperatingSystem.MACOS,)),#adding a comma for one item tuple
    Person(name="Fatma", age= 22, preferred_operating_systems=(OperatingSystem.UBUNTU,OperatingSystem.ARCH)),    
    Person(name="Muhib", age= 19, preferred_operating_systems=(OperatingSystem.MACOS,OperatingSystem.UBUNTU)),    

]


# Updated based on feedback: 
# Instead of hard‑coding sadness scores (0, 1, 2), this version uses the 
# position of the laptop’s OS in the person’s preference list to decide the sadness value. 
# I check for membership first (so no exceptions), then 
# use the index as the rank. Only the top MAX_HAPPY_RANK preferences count; 
# anything lower or not listed gets a high penalty. 

MAX_HAPPY_RANK = 3
TERRIBLE_SADNESS = 100
def sadness(person: Person, laptop: Laptop) -> int:
    prefs = person.preferred_operating_systems

    if laptop.operating_system not in prefs:
        return TERRIBLE_SADNESS

    rank = prefs.index(laptop.operating_system)

    return rank if rank < MAX_HAPPY_RANK else TERRIBLE_SADNESS

    #Allocate laptops to people in a way that minimises total sadness.
    #Builds a cost matrix using the sadness() function and applies the
    #Hungarian algorithm (linear_sum_assignment) to find the optimal
    #one‑to‑one assignment between people and laptops.

    
def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    n_people = len(people) #length of people []
    n_laptops = len(laptops) #length of laptops []
    if n_laptops < n_people:
        raise ValueError("Not enough laptops to allocate one to each person.")
    sadness_matrix = np.zeros((n_people, n_laptops), dtype= int)  #npzero mean each cell in 2d grid is a zero and dtype is datatype int so it int 0
    for i, person in enumerate(people): #enumerate gives us both index position and the item itself from the list 
        for j, laptop in enumerate(laptops):
            sadness_matrix[i,j] = sadness(person, laptop) #this matrix represents complete laptop allocation 
            # Hungarian algorithm to run on our sadness matrix
    row_indices, col_indices = linear_sum_assignment(sadness_matrix) #which person which laptop
        # Map people to laptops
    allocation: Dict[Person, Laptop] = {}
    for i, j in zip(row_indices, col_indices):#it pairs up results (person indices and laptop indices). The loop then uses those pairs to build the final allocation dictionary
        allocation[people[i]] = laptops[j]
    return allocation


def print_allocation(allocation: Dict[Person, Laptop]):
    for person, lap in allocation.items():
        print(f"{person.name} gets Laptop {lap.id} ({lap.operating_system.value})")

allocation = allocate_laptops(people, laptops)
print_allocation(allocation)
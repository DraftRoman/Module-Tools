from dataclasses import dataclass
from enum import Enum
from typing import List
from typing import Dict

# ============================================================================
# ENUM DEFINITIONS
# ============================================================================
class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

# ============================================================================
# DATA CLASSES
# ============================================================================
@dataclass(frozen=True)
class Person:
    name: str
    age: int
    # Sorted in order of preference, most preferred is first.
    preferred_operating_system: tuple


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

# ============================================================================
# HELPER FUNCTION
# ============================================================================
"""
    Calculates how "sad" a person would be with a given laptop allocation.
    
    Sadness is defined as the position (0-indexed) of the laptop's OS
    in the person's preference list. For example:
    - If preferences are [UBUNTU, ARCH, MACOS] and they get UBUNTU: sadness = 0
    - If preferences are [UBUNTU, ARCH, MACOS] and they get ARCH: sadness = 1
    - If preferences are [UBUNTU, ARCH, MACOS] and they get MACOS: sadness = 2
    - If they get an OS not in their preferences: sadness = 100
    
    Args:
        person: The person receiving the laptop
        laptop: The laptop being allocated
        
    Returns:
        An integer representing sadness (0 = most happy, 100 = not in preferences)
    """

def calculate_sadness(person:Person, laptop:Laptop)-> int:
     if laptop.operating_system in person.preferred_operating_system:
         # Find the index (position) of this OS in their preference list
         sadness = person.preferred_operating_system.index(laptop.operating_system)
         return sadness
     else:
         # OS not in preferences = very sad
         return 100
   
# ============================================================================
# TEST DATA
# ============================================================================

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, 
           operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, 
           operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, 
           operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, 
           operating_system=OperatingSystem.MACOS),
    Laptop(id=5, manufacturer="Apple", model="macBook Pro", screen_size_in_inches=16, 
           operating_system=OperatingSystem.MACOS),
    Laptop(id=6, manufacturer="Lenovo", model="ThinkPad", screen_size_in_inches=14, 
           operating_system=OperatingSystem.UBUNTU),
    Laptop(id=7, manufacturer="System76", model="Lemur Pro", screen_size_in_inches=15, 
           operating_system=OperatingSystem.ARCH),
    Laptop(id=8, manufacturer="Framework", model="Framework 13", screen_size_in_inches=13, 
           operating_system=OperatingSystem.UBUNTU),
]

people = [
    Person(name="Imran", age=22, preferred_operating_system=(OperatingSystem.UBUNTU, OperatingSystem.MACOS)),
    Person(name="Eliza", age=34, preferred_operating_system=(OperatingSystem.ARCH, OperatingSystem.UBUNTU)),
    Person(name="Marcus", age=28, preferred_operating_system=(OperatingSystem.MACOS, OperatingSystem.UBUNTU)),
    Person(name="Sofia", age=31, preferred_operating_system=(OperatingSystem.UBUNTU,)),
    Person(name="James", age=25, preferred_operating_system=(OperatingSystem.ARCH, OperatingSystem.MACOS)),
    Person(name="Nina", age=29, preferred_operating_system=(OperatingSystem.MACOS, OperatingSystem.ARCH, OperatingSystem.UBUNTU)),
]



# ============================================================================
# TESTING
# ============================================================================

def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person,Laptop]:

    if len(laptops) < len(people):
         raise ValueError("Not enough laptops to allocate one per person")
    

    people_sorted = sorted(people, key = lambda p: len(p.preferred_operating_system))
         
    result={}
    available_laptops = laptops.copy()

    for person in people_sorted:
        smallest_sadness = float("inf")
        best_laptop = None

        for laptop in available_laptops:
            sadness = calculate_sadness(person, laptop)
            if sadness < smallest_sadness:
                smallest_sadness = sadness 
                best_laptop = laptop


            if smallest_sadness == 0:
                break

        result[person]= best_laptop  
        available_laptops.remove(best_laptop)      

    return result


allocation = allocate_laptops(people, laptops)

print("\n" + "="*50)
print("FINAL ALLOCATION:")
print("="*50)
for person, laptop in allocation.items():
    print(f"{person.name}: {laptop.manufacturer} {laptop.model} ({laptop.operating_system.value})")




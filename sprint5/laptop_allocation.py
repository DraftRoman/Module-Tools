from dataclasses import dataclass
from enum import Enum
from typing import List,Dict,Tuple


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: Tuple[OperatingSystem, ...]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

# calculate sadness score
def calculate_sadness(person:Person,laptop:Laptop) -> int:
    if laptop.operating_system in person.preferred_operating_system:
        sadness=person.preferred_operating_system.index(laptop.operating_system)
        return sadness
    else:
        return 100
    
def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    if len(laptops) < len(people):
        raise ValueError("Not enough laptops")

    total=float("inf")    # store the min sadness
    allocation:Dict[Person, Laptop]={} # store best allocation
    
    # try all possible laptop combinations
    def find_best_allocation(person_index:int,current_total:int,current_allocation: Dict[Person, Laptop],remaining_laptops: List[Laptop]):
        nonlocal total, allocation
        if person_index == len(people): # everybody have a laptop 

            if current_total<total: # check if this allocation is better
                total=current_total
                allocation=current_allocation.copy()
            return
        
        person=people[person_index] # get current person

        for laptop in remaining_laptops:
            sadness=calculate_sadness(person,laptop) 
            current_allocation[person]=laptop

            find_best_allocation(person_index+1,current_total+sadness,current_allocation,[l for l in remaining_laptops if l !=laptop])
            del current_allocation[person]

    find_best_allocation(0,0,{},laptops) 
           
    return allocation

if __name__ == "__main__":
    people = [
        Person("Imran", 22, (OperatingSystem.UBUNTU,)),
        Person("Eliza", 34, (OperatingSystem.ARCH,)),
    ]

    laptops = [
        Laptop(1, "Dell", "XPS", 13, OperatingSystem.ARCH),
        Laptop(2, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
        Laptop(3, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
        Laptop(4, "Apple", "MacBook", 13, OperatingSystem.MACOS),
    ]

    result = allocate_laptops(people, laptops)

    print("Allocation result:")
    total = 0
    for person, laptop in result.items():
        s = calculate_sadness(person, laptop)
        total += s
        print(f"{person.name} -> {laptop.model} ({laptop.operating_system.value}) | sadness={s}")

    print("Total sadness:", total)


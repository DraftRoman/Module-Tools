from dataclasses import dataclass
from enum import Enum
from typing import List


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def find_possible_laptops(laptops: List[Laptop], os: OperatingSystem) -> List[Laptop]:
    return [l for l in laptops if l.operating_system == os]


def count_laptops_by_os(laptops: List[Laptop]) -> dict[OperatingSystem, int]:
    counts = {os: 0 for os in OperatingSystem}
    for laptop in laptops:
        counts[laptop.operating_system] += 1
    return counts


def parse_operating_system(user_input: str) -> OperatingSystem:
    normalized = user_input.strip().lower()

    mapping = {
        "macos": OperatingSystem.MACOS,
        "mac": OperatingSystem.MACOS,
        "arch": OperatingSystem.ARCH,
        "arch linux": OperatingSystem.ARCH,
        "ubuntu": OperatingSystem.UBUNTU,
    }

    if normalized not in mapping:
        raise ValueError("Invalid operating system")

    return mapping[normalized]


laptops = [
    Laptop(1, "Dell", "XPS", 13, OperatingSystem.ARCH),
    Laptop(2, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
    Laptop(3, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
    Laptop(4, "Apple", "MacBook", 13, OperatingSystem.MACOS),
]

name = input("Enter your name: ")
age = int(input("Enter your age: "))
os_input = input("Preferred OS (macOS / Arch / Ubuntu): ")

try:
    preferred_os = parse_operating_system(os_input)
except ValueError:
    print("Invalid OS entered. Exiting.")
    exit()

person = Person(name=name, age=age, preferred_operating_system=preferred_os)

matching_laptops = find_possible_laptops(laptops, person.preferred_operating_system)
counts = count_laptops_by_os(laptops)

print(f"\nHello {person.name}!")
print(f"We have {len(matching_laptops)} laptop(s) with {person.preferred_operating_system.value}.")

# --- Suggest better option ---
best_os = max(counts, key=counts.get)

if best_os != person.preferred_operating_system:
    print(
        f"If you're open to {best_os.value}, "
        f"you'll have a higher chance ({counts[best_os]} available)."
    )
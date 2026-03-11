import unittest
from laptop_allocation import allocate_laptops, Person, Laptop, OperatingSystem, unpreferred_OS_penalty

laptops = [
    Laptop(1, "Dell", "XPS 13", 13, OperatingSystem.ARCH),
    Laptop(2, "HP", "Spectre 15", 15, OperatingSystem.UBUNTU),
    Laptop(3, "Lenovo", "ThinkPad 14", 14, OperatingSystem.UBUNTU),
    Laptop(4, "Apple", "MacBook Air", 13, OperatingSystem.MACOS),
    Laptop(5, "Apple", "MacBook Pro", 16, OperatingSystem.MACOS),
    Laptop(6, "Dell", "Latitude", 15, OperatingSystem.ARCH),
    Laptop(7, "HP", "EliteBook", 13, OperatingSystem.MACOS),
    Laptop(8, "Lenovo", "Yoga", 14, OperatingSystem.UBUNTU)
]

people = [
    Person("Alice", 29, (OperatingSystem.UBUNTU, OperatingSystem.MACOS)),
    Person("Bob", 34, (OperatingSystem.ARCH, OperatingSystem.UBUNTU)),
    Person("Charlie", 40, (OperatingSystem.MACOS, OperatingSystem.ARCH)),
    Person("Diana", 25, (OperatingSystem.MACOS,)),
    Person("Ethan", 31, (OperatingSystem.UBUNTU, OperatingSystem.ARCH)),
    Person("Fiona", 27, (OperatingSystem.MACOS, OperatingSystem.UBUNTU)),
    Person("George", 22, (OperatingSystem.ARCH, OperatingSystem.MACOS)),
    Person("Zara", 33, (OperatingSystem.ARCH, OperatingSystem.MACOS))
]

class TestLaptopAllocation(unittest.TestCase):
    
    def setUp(self):
        self.assignment = allocate_laptops(people, laptops)
    
    def test_everyone_has_laptop(self):
        assigned_people = set(self.assignment.keys())
        self.assertEqual(assigned_people, set(people), "Some people are missing a laptop")
    
    def test_no_duplicate_laptops(self):
        assigned_laptop_ids = [laptop.id for laptop in self.assignment.values()]
        self.assertEqual(len(assigned_laptop_ids), len(set(assigned_laptop_ids)), "Duplicate laptops assigned")
    
    def test_sadness_scores(self):
        for person, laptop in self.assignment.items():
            if laptop.operating_system in person.preferred_operating_system:
                score = person.preferred_operating_system.index(laptop.operating_system)
                self.assertGreaterEqual(score, 0, f"Negative score for {person.name}")
            else:
                self.assertEqual(unpreferred_OS_penalty, 100, f"Unexpected unpreferred penalty for {person.name}")
    
    def test_total_sadness(self):
        total_sadness = sum(
            person.preferred_operating_system.index(laptop.operating_system)
            if laptop.operating_system in person.preferred_operating_system else unpreferred_OS_penalty
            for person, laptop in self.assignment.items()
        )
        calculated_sadness = sum(
            person.preferred_operating_system.index(laptop.operating_system)
            if laptop.operating_system in person.preferred_operating_system else unpreferred_OS_penalty
            for person, laptop in self.assignment.items()
        )
        self.assertEqual(total_sadness, calculated_sadness, "Total sadness mismatch")

if __name__ == "__main__":
    unittest.main()

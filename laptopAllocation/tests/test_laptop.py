
#If a person gets a laptop with their first‑choice operating system, their sadness should be 0.
from laptop import Person, Laptop, OperatingSystem, sadness

def test_sadness_first_choice():
    person = Person("Test", 20, (OperatingSystem.MACOS,))
    laptop = Laptop(1, "Apple", "macBook", 13, OperatingSystem.MACOS)

    assert sadness(person, laptop) == 0
from laptop import Person, Laptop, OperatingSystem, sadness, TERRIBLE_SADNESS
#Adding more tests 
def test_sadness_second_choice():
    person = Person("Test", 20, (OperatingSystem.MACOS, OperatingSystem.UBUNTU))
    laptop = Laptop(1, "Dell", "XPS", 13, OperatingSystem.UBUNTU)
    assert sadness(person, laptop) == 1


def test_sadness_not_in_preferences():
    person = Person("Test", 20, (OperatingSystem.MACOS,))
    laptop = Laptop(1, "Dell", "XPS", 13, OperatingSystem.UBUNTU)
    assert sadness(person, laptop) == TERRIBLE_SADNESS


def test_sadness_above_max_rank():
    # as our MAX_HAPPY_RANK = 3, so rank 3 should be TERRIBLE_SADNESS
    person = Person(
        "Test", 20,
        (OperatingSystem.MACOS, OperatingSystem.UBUNTU, OperatingSystem.ARCH)
    )
    laptop = Laptop(1, "Dell", "XPS", 13, OperatingSystem.ARCH)
    assert sadness(person, laptop) == TERRIBLE_SADNESS

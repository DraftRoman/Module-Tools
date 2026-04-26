def half(value):
    return value / 2 

def double(value):
    return value * 2 

def second(value):
    return value[1]

print(double(22))
print(double("hello"))
print(double("22")) #returns "2222" because concatenation of strings. 
# I thought it would fail because of the type mismatch
# $ mypy prep.py 
# Success: no issues found in 1 source file


def open_account(balances: dict[str, int], name: str, amount: float):
    balances[name] = int(amount * 100)

def sum_balances(accounts: dict[str, int]) -> int:
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_string(total_pence: int) -> str:
    if total_pence < 100:
        return f"{total_pence}p"
    pounds = int(total_pence / 100)
    pence = total_pence % 100
    return f"£{pounds}.{pence:02d}"

balances = {
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}

open_account(balances, "Tobi", 9.13) # Mist balances and this is a float, but we want to store pence as an integer.
open_account(balances, "Olya", 7.13) # Mist balances and this is a float, but we want to store pence as an integer.

total_pence = sum_balances(balances) 
total_string = format_pence_as_string(total_pence)

print(f"The bank accounts total {total_string}")
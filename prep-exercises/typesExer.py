from typing import Union, Dict


def open_account(balances: Dict[str, int], name: str, amount: Union[str, float]):
    balances[name] = int(float(amount) *100)

def sum_balances(accounts: Dict[str, int]):
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_pound(total_pence: int) -> str:
    if total_pence < 100:
        return f"{total_pence}p"
    pounds = total_pence // 100
    pence = total_pence % 100
    return f"£{pounds}.{pence:02d}"

balances = {
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}

open_account(balances, "Tobi", 9.13)
open_account(balances, "Olya", 7.13)

total_pence = sum_balances(balances)
total_pound = format_pence_as_pound(total_pence)

print(f"The bank accounts total {total_pound}")
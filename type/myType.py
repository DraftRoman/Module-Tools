def triple(number : int)-> int:
    return number * 3

print(triple(10))

# Bank account functions


def open_account( name:str, amount:float)->None:
    balances[name] = int(amount * 100  )



def sum_balances(accounts: dict[str, int]) -> int:
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_string(total_pence: int)->str:
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
open_account("Tobi", 9.13)
open_account("Olya", 7.13)

total_pence = sum_balances(balances)
total_string = format_pence_as_string(total_pence)

print(f"The bank accounts total {total_string}")
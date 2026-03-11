
from typing import Dict
def open_account(balances: Dict[str,int], name:str, amount:int)->None: #dic type str and int--- returns none/figured after running --strict flag with mypy
    #Adding a new account 
    balances[name] = amount

def sum_balances(accounts:Dict[str,int])-> int: #takes type dic[str, int}returns int
    total = int = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_string(total_pence: int)-> str: #type int returns type str
    #formatting pence as a string 
    sign = "-" if total_pence < 0 else ""
    total_pence = abs(total_pence)

    if total_pence < 100:
        return f"{sign}{total_pence}p"
    pounds =(total_pence // 100)  #floordivision always returns an int
    pence = total_pence % 100
    return f"{sign}£{pounds}.{pence:02d}"

balances:Dict[str,int]  = {             #dic type {str:int}
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}

open_account(balances,"Tobi", 913) # correct passing of the argumenst to functions with balances.
open_account(balances,"Olya", 713)

total_pence = sum_balances(balances)  #returntype int
total_string = format_pence_as_string(total_pence) #returntype str and wrong function name

print(f"The bank accounts total {total_string}")
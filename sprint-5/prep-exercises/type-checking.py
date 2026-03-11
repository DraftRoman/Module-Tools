# This code contains bugs related to types. They are bugs mypy can catch.

# Read this code to understand what it’s trying to do. Add type annotations to the method parameters and return types of this code. Run the code through mypy, and fix all of the bugs that show up. When you’re confident all of the type annotations are correct, and the bugs are fixed, run the code and check it works.

            # def open_account(balances, name, amount):
            #     balances[name] = amount

            # def sum_balances(accounts):
            #     total = 0
            #     for name, pence in accounts.items():
            #         print(f"{name} had balance {pence}")
            #         total += pence
            #     return total

            # def format_pence_as_string(total_pence):
            #     if total_pence < 100:
            #         return f"{total_pence}p"
            #     pounds = int(total_pence / 100)
            #     pence = total_pence % 100
            #     return f"£{pounds}.{pence:02d}"

            # balances = {
            #     "Sima": 700,
            #     "Linn": 545,
            #     "Georg": 831,
            # }

            # open_account("Tobi", 9.13)
            # open_account("Olya", "£7.13")

            # total_pence = sum_balances(balances)
            # total_string = format_pence_as_str(total_pence)

            # print(f"The bank accounts total {total_string}")

#when I run mypy on this code, it shows several type errors related to the parameters passed to the open_account function. 
        # type-checking.py:5: error: Function is missing a type annotation  [no-untyped-def]
        # type-checking.py:8: error: Function is missing a type annotation  [no-untyped-def]
        # type-checking.py:15: error: Function is missing a type annotation  [no-untyped-def]
        # type-checking.py:28: error: Call to untyped function "open_account" in typed context  [no-untyped-call]
        # type-checking.py:28: error: Missing positional argument "amount" in call to "open_account"  [call-arg]
        # type-checking.py:29: error: Call to untyped function "open_account" in typed context  [no-untyped-call]
        # type-checking.py:29: error: Missing positional argument "amount" in call to "open_account"  [call-arg]
        # type-checking.py:31: error: Call to untyped function "sum_balances" in typed context  [no-untyped-call]
        # type-checking.py:32: error: Name "format_pence_as_str" is not defined  [name-defined]
        # Found 9 errors in 1 file (checked 1 source file)
#To fix these errors, In the open_account function I need to ensure that the balances parameter is a dictionary mapping strings to integers, the name parameter is a string, and the amount parameter is an integer .
#Additionally, I need to make sure that the values passed to the open_account function are of the correct types.
#Here is the corrected code with type annotations and fixed function calls:         

from typing import Dict

def open_account(balances: Dict[str, int], name: str, amount: int) -> None:
    balances[name] = amount

def sum_balances(accounts: Dict[str, int]) -> int:
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_string(total_pence: int) -> str:
    negative = total_pence < 0
    total_pence = abs(total_pence)

    if total_pence < 100:
        result = f"{total_pence}p"
    else:
        pounds = total_pence // 100
        pence = total_pence % 100
        result = f"£{pounds}.{pence:02d}"

    return f"-{result}" if negative else result

balances: Dict[str, int] = {
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}

open_account(balances, "Tobi", 913)  
open_account(balances, "Olya", 713)
open_account(balances, "Alex", -250)

total_pence = sum_balances(balances)
total_string = format_pence_as_string(total_pence) 

print(f"The bank accounts total {total_string}")

# Now, when I run mypy on the corrected code, I get no type errors, indicating that all type annotations are correct and the bugs have been fixed.with the result:"# Success: no issues found in 1 source file"
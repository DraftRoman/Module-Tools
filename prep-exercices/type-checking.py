# his code contains bugs related to types. They are bugs mypy can catch.

# Read this code to understand what it’s trying to do.
# Add type annotations to the method parameters and return types of this code.
# Run the code through mypy, and fix all of the bugs that show up. 
# When you’re confident all of the type annotations are correct, and the bugs are fixed, run the code and check it works.


 
def open_account(balances, name, amount):
    balances[name] = amount

def sum_balances(accounts):
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_string(total_pence):
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

# convert pounds to pence
open_account(balances, "Tobi", int(9.13 * 100))   # 913 pence
open_account(balances, "Olya", int(7.13 * 100))   # 713 pence

total_pence = sum_balances(balances)
total_string = format_pence_as_string(total_pence)

print(f"The bank accounts total {total_string}")




# When running mypy, I get the following errors:

# type-checking.py:24: error: Missing positional argument "amount" in call to "open_account"  [call-arg]
# type-checking.py:25: error: Missing positional argument "amount" in call to "open_account"  [call-arg]
# type-checking.py:28: error: Name "format_pence_as_str" is not defined  [name-defined]
# type-checking.py:34: error: Missing positional argument "amount" in call to "open_account"  [call-arg]
# type-checking.py:35: error: Missing positional argument "amount" in call to "open_account"  [call-arg]
# type-checking.py:38: error: Name "format_pence_as_str" is not defined  [name-defined]


# To fix this code, I need to add type annotations and correct the function calls as follows:

# wrong arguments to open_account, the function expects three arguments: balances, name, and amount.
# one call passes a string "£7.13" instead of a number.
# Wrong function name format_pence_as_str instead of format_pence_as_string.
# To keep the program consistent (Everything in pence), convert pounds to pence when opening accounts.

# Here is the corrected code:

"""
def open_account(balances, name, amount):
    balances[name] = amount

def sum_balances(accounts):
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_string(total_pence):
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

# convert pounds to pence
open_account(balances, "Tobi", int(9.13 * 100))   # 913 pence
open_account(balances, "Olya", int(7.13 * 100))   # 713 pence

total_pence = sum_balances(balances)
total_string = format_pence_as_string(total_pence)

print(f"The bank accounts total {total_string}")
"""


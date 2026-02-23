# ✍️exercise
# Do not run the following code.

# This code contains bugs related to types. They are bugs mypy can catch.

# Read this code to understand what it’s trying to do. 
# Add type annotations to the method parameters and return types of this code. 
# Run the code through mypy, and fix all of the bugs that show up. 
# When you’re confident all of the type annotations are correct, and the bugs are fixed, 
# run the code and check it works.

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
# File "C:\Users\kkazi\Desktop\cyf\Module-Tools\prep\3.py", line 27, in format_pence_as_string
   # return f"£{pounds}.{pence:02d}"
                       #^^^^^^^^^^^
#ValueError: Unknown format code 'd' for object of type 'float'
balances = {
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}

open_account(balances, "Tobi", 913) # to solve the float int issue value passed in in pence3.py:35: error: Missing positional argument "amount" in call to "open_account"  [call-arg]
open_account(balances, "Olya", 713) #3.py:36: error: Missing positional argument "amount" in call to "open_account"  [call-arg]

total_pence = sum_balances(balances)
total_string = format_pence_as_string(total_pence) # 3.py:39: error: Name "format_pence_as_str" is not defined  [name-defined]
print(f"The bank accounts total {total_string}")
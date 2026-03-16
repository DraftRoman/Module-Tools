# def double(number):
#     return number * 3

# print(double(10))


# --- Exercise ---
# Read the above code and write down what the bug is. How would you fix it?


# --- Solution ---
# The bug in the code is that the function is named "double" but actually triples the input number instead of doubling it. 

# To fix it, the multiplication should be changed from 3 to 2 or the naming of the function should change to "triple".

# Here is the corrected code:

def double(number): 
    return number * 2 

# OR

# def triple(number): 
#     return number * 3
def double(value):
    return value * 2 

print(double("22"))

#exercise 1:
# Predict what double("22") will do. Then run the code and check. Did it do what you expected? Why did it return the value it did?

#solution:
# My prediction is that it will return "44" but 
# when I run the code I got "2222" which is different from my prediction 
# because the function takes the string "22"  concatenates it with itself, resulting in "2222". When you multiply a string by an integer in Python, it repeats the string that many times.



#exercise 2:
#Read the code and write down what the bug is. How would you fix it?
def double(number):
    return number * 3

print(double(10))

#solution:
# The bug is that the function is supposed to double the input value, but it is actually tripling it by multiplying by 3. 
# To fix it, I would change the multiplication factor from 3 to 2, like this:

# def double(number):
#     return number * 2             or

# I would rename the function to reflect its actual behavior:

# def triple(number):
#     return number * 3

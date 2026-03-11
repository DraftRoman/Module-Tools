# ------------------------
# Exercise 1
# ------------------------
# Q. What does double("22") return? Did it do what you expected? Why did it return the value it did?
# A. I expected the result to be 44 through coercion, like JavaScript.
#    It returned the string repeated i.e. 2222 because Python is a strongly typed language and doesn't use coercion

def double(input):
    return input * 2

print(double("22")) # returns "2222"



# ------------------------
# Exercise 2
# ------------------------
# Q. Read the code and write down what the bug is. How would you fix it?
# A. In this function it returns the value of 30, which is the input * 3 which is logically correct, however you would 
#    expect the function to be called "triple" or you would expect the logic to be number * 2, so i would amend 
#    the function to either of these solutions

# original function (buggy):
def double(number):
    return number * 3

print(double(10)) # returns "30"


#  solution 1 - fix the logic:
def double(number):
    return number * 2

print(double(10))  # returns "20"



#  solution 2 - rename the function:
def triple(number):
    return number * 3

print(triple(10))  # returns "30"
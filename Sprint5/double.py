def double(n): 
    return n*2
num = double("22")
print(num)

#my prediction is that it would return 2222. As python will treat 22 as a string being a strongly typed language.
#if it was javascript * operator would have forced numeric converion and 22 string would have become 22 int and 44 would 
#have been returned
# when I run the file it returns 2222 as expected.

# 2nd exercise- original function :
def double(number):
    return number * 3

print(double(10)) # returns "30"

#so we either change the name of the function to triple or multiply number with 2 rather than 3 
def triple(number):
    return number * 3

print(triple(10)) # returns "30"
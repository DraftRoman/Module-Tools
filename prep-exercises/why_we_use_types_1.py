def half(value):
    return value / 2 

def double(value):
    return value * 2 

def second(value):
    return value[1]

print(double("22"))


# --- Exercise ---
# Predict what double("22") will do. Then run the code and check. Did it do what you expected? Why did it return the value it did?


# --- Solution ---
# My prediction is that double("22") would return an error because "22" is a string and multiplying a string by 2 might not be valid.

# The function double("22") will return "2222". This is because in Python, multiplying a string by an integer results in the string being repeated that many times. I did also change the * 2 to * 3 to see how it worked. So when we multiply the string "22" by 2, it concatenates "22" with itself, resulting in "2222".

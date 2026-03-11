# def double(n: int) -> int:
#     return n * 2

# num = double(21)
# print(num)



from typing import List, Dict, Counter, Set, Union, Any
from math import sqrt


def average(nums: List[int]) -> float:
    total = sum(nums)
    count = len(nums)
    return total / count

print(average([1, 2, 3, 4])) # 2.5


# from typing import Dict
def get_total_marks(scorecard: Dict[str, int]) -> int:
    marks = list(scorecard.values())  # marks : List[int]
    return sum(marks)

scores = {'english': 84, 'maths': 92, 'history': 75}
print(get_total_marks(scores))  # 251


# from typing import Counter, List
def count_occurences(data: List[float]) -> Counter[float]:
  occurences = Counter(data)
  return occurences

nums = [2.5, 1.0, 7, 1, 6, 2.5, 1.0]
print(count_occurences(nums))  # Counter({1.0: 3, 2.5: 2, 7: 1, 6: 1})


# from typing import List
def unique_count(nums: List[int]) -> int:
    """counts the number of unique items in the list"""
    uniques = set()  # How does mypy know what type this is?
    for num in nums:
        uniques.add(num)

    return len(uniques)

print(unique_count([1, 2, 1, 3, 1, 2, 4, 3, 1]))  # 4


# from typing import List, Set
def unique_count(nums: List[int]) -> int:
    """counts the number of unique items in the list"""
    uniques: Set[int] = set()  # Manually added type information
    for num in nums:
        uniques.add(num)

    return len(uniques)

print(unique_count([1, 2, 1, 3, 1, 2, 4, 3, 1]))  # 4


# from typing import List, Set
def unique_count(nums: List[int]) -> int:
    """counts the number of unique items in the list"""
    uniques: Set[int] = set()
    for num in nums:
        uniques.add(num)

    return len(uniques)

counts = unique_count([1, 2, 1, 3, 1, 2, 4, 3, 1])

reveal_type(counts)  # The special magic reveal_type method - 
# you should only use reveal_type to debug your code, and remove it when you're done debugging.


def print_favorite_color(person):
    fav_color = person.get('favorite-color')
    if fav_color is None:
        print("You don't have a favorite color. 😿")
    else:
        print(f"Your favorite color is {fav_color}! 😸.")

me = {'name': 'Tushar', 'favorite-color': 'Purple'}
print_favorite_color(me)


def print_favorite_color(person: Dict[str, str]) -> None:  # added types to function definition
    fav_color = person.get('favorite-color')
    reveal_type(fav_color)  # added this line here
    if fav_color is None:
        print("You don't have a favorite color. 😿")
    else:
        print(f"Your favorite color is {fav_color}! 😸.")

me = {'name': 'Tushar', 'favorite-color': 'Purple'}
print_favorite_color(me) 


def print_item(item):
    if isinstance(item, list):
        for data in item:
            print(data)
    else:
        print(item)

print_item('Hi!')
print_item(['This is a test', 'of polymorphism'])


def print_item(item: Union[str, List[str]]) -> None:
    reveal_type(item)
    
    if isinstance(item, list):
        for data in item:
            reveal_type(item)
            print(data)
    else:
        reveal_type(item)
        print(item)

print_item('Hi!')
print_item(['This is a test', 'of polymorphism'])


#a type-annotated Python implementation of the builtin function abs:
def my_abs(num: Union[int, float, complex]) -> float:
    if isinstance(num, complex):
        # absolute value of a complex number is sqrt(i^2 + j^2)
        return sqrt(num.real ** 2 + num.imag ** 2)

    else:
        return num if num > 0 else -num

print(my_abs(-5.6))  # 5.6
print(my_abs(42))    # 42
print(my_abs(0))     # 0
print(my_abs(6-8j))  # 10.0


# if you ever try to run reveal_type inside an untyped function, this is what happens:
def average(nums):
    total = sum(nums)
    count = len(nums)

    ans = total / count
    reveal_type(ans)  # revealed type says it is 'Any' - 'Any' turns off type checking - so, avoid it if poss!


def post_data_to_api(data: Any) -> None:
    requests.post('https://example.com/post', json=data)

data = '{"num": 42, "info": null}'
parsed_data = json.loads(data)
reveal_type(parsed_data)  # Revealed type is 'Any'

post_data_to_api(data)
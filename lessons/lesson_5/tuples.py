from typing import Any

my_tuple: tuple[int, ...] = (1, 2, 3, 4, 5)

my_tuple_v2 = 1, 2, 3, 4, 5 # не прийнято так робити

my_tuple_one_element = (1,)

empty_tuple: tuple = ()
empty_tuple_v2: tuple[Any, ...] = tuple()


# -----------------------------------------

my_mixed_tuple: tuple[Any, ...] = (1, "2", 3.5, True, None, ["one", None, "two", "three"], [], (5,), {"one": 1}, None)

my_mixed_tuple[5].append("four")
print(my_mixed_tuple)

# indexation
third_element = my_mixed_tuple[2]
last_element = my_mixed_tuple[-1]

# slicing
sliced_tuple: tuple[Any, ...] = my_mixed_tuple[0:2] # from first to third elements
slice_tuple_evens = my_mixed_tuple[1::2]

three = my_mixed_tuple[5][-1]

# my_mixed_tuple[0] = 100

# count
count_of_none_elements: int = my_mixed_tuple.count(None)

# print(count_of_none_elements)

print(my_mixed_tuple.count([]))

# .index()

none_first_index: int = my_mixed_tuple.index(None)
none_last_index: int = my_mixed_tuple.index(None, none_first_index + 1)


# print(none_first_index)
# print(none_last_index)

# CONST
BASE_URL = "https://www.google.com"


my_string = f"{BASE_URL}/search?q=hbfhew?o=njknejh"

tuple_of_letters: tuple[str, ...] = tuple(my_string)









list_of_numbers: list[int] = [1, 2, 3, 4, 5]
list_of_random_numbers: list[float] = [1000, True, [], (50,), {"one": 1}, None, "Some string", {5, 5}]
print(id(list_of_random_numbers), list_of_random_numbers)

empty_list: list = [] # recommended
empty_list_v2: list[int] = list()

first_element = list_of_numbers[0]
last_element = list_of_numbers[-1]
forth_element = list_of_numbers[3]

from_second_to_fourth_elements = list_of_numbers[1:4]
from_third_to_end_elements = list_of_numbers[2:]

list_of_random_numbers[1] = False
list_of_random_numbers[4], list_of_random_numbers[0] = list_of_random_numbers[0], list_of_random_numbers[4]
print(id(list_of_random_numbers), list_of_random_numbers)

my_string = "Some string"


# converting to list
list_of_chars: list[str] = list(my_string)
print(list_of_chars)

my_tuple_random = (1, "two", False)
list_from_tuple: list = list(my_tuple_random)

my_dict = {
    "one": 1,
    "two": 2,
    "three": 3
}

list_from_dict: list = list(my_dict)
print(list_from_dict)


list_of_random_numbers: list[float] = [1000, True, [], (50,), {"one": 1}, None, "Some string", {5, 5}]

#counting
count_of_empty_lists = list_of_random_numbers.count([])
print(count_of_empty_lists)

#index search
index_of_none = list_of_random_numbers.index("string")
print(index_of_none)



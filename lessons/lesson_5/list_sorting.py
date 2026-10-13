list_of_random_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -90, 33.2, 1.2]


list_of_random_numbers.sort(reverse=True) # method

sorted_list_of_random_numbers = sorted(list_of_random_numbers, reverse=True) # global function

print(list_of_random_numbers)
print(sorted_list_of_random_numbers)


list_of_names = ["John", "Jane", "Bo", "Alexandr", "Zoe", "Abibas"]

list_of_names.sort(reverse=True, key=len) # [len("John"), len("Jane"), len("Bo"), len("Alexandr"), len("Zoe"), len("Abibas")]
# [4, 4, 2, 7, 4, 5]

print(list_of_names)


list_of_persons = [
    ("John", 20),
    ("Jane", 21),
    ("Bo", 22),
    ("Alexandr", 23),
    ("Zoe", 24),
    ("Abibas", 25)
]
sorted_list_of_persons = sorted(list_of_persons, key=lambda element: element[-1]) # ("John", 20)[1], ("Jane", 21)[1], ...
print(sorted_list_of_persons)

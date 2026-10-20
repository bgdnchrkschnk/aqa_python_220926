# list_from_1_10 = list(range(1, 101))
#
# # ------------------------------------------
#
#
# list_with_values = []
#
# for value in list_from_1_10:
#     if value % 2 == 0:
#         list_with_values.append(value)
#
#
# print(list_with_values)

# ------------------------------------ FILTRATION, GENERATION

l_comprehension: list = [value for value in range(1, 101) if value % 2 == 0]

print(l_comprehension)


users_list: list[dict] = [
    {"name": "John", "age": 20, "sex": "male"},
    {"name": "Mary", "age": 21, "sex": "female"},
    {"name": "Bob", "age": 22, "sex": None},
    {"name": "Nick", "age": 23},
]

# filtration by only males

users_list_filtered: list[dict] = [user for user in users_list if user.get('sex') == "male"]

print(users_list_filtered)




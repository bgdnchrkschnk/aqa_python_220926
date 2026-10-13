my_list = [1, 2, 3, 4, 5]
# print(id(my_list))


# add element to the end
my_list.append(6)
my_list.append(7)
my_list.append(6)
my_list.append([6, 7, 6])
# print(id(my_list))

# concatenation
str_1 = "Hello, "
str_2 = "World!"

# print(id(str_1))
# print(id(str_2))
final_string = str_1 + str_2

# print(id(final_string))


# list concatenation
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print(id(list_1))
print(id(list_2))

list_1.extend(list_2)

print(id(list_1))


# ---------------------------------- concatenate lists

sum_of_lists = list_1 + list_2 + my_list

print(sum_of_lists)

# ------------------------------------- pop

last_deleted_element = sum_of_lists.pop()
first_deleted_element = sum_of_lists.pop(0)

print(first_deleted_element)
print(sum_of_lists)

# ---------------- remove

sum_of_lists.remove(6)
print(sum_of_lists)

# ---------------- clear

# sum_of_lists = []
# sum_of_lists.clear()

# ---------------- insert

sum_of_lists.insert(0, "First element")
print(sum_of_lists)



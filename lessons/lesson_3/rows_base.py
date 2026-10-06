one_line_v1: str = ('This is one line string. '
                    'It used for saving some text data inside. '
                    'One quotation mark version looks like that. '
                    'You can you like that')
one_line_v2: str = ("This is one line string. 5 True, None "
                    "It used for saving some text data inside. "
                    "One quotation mark version looks like that. "
                    "You can you like that")


three_line_str_v1: str = """This is one line string. 
5 True, None It used for saving some text data inside. 
One quotation mark version looks like that. 
You can you like that""" # тут три фізичних лінії, проте лише одна логічна лінія

three_line_str: str = '''This is one line string. 
5 True, None It used for saving some text data inside. 
One quotation mark version looks like that. 
You can you like that''' # тут три фізичних лінії, проте лише одна логічна лінія



print(one_line_v1)
print(one_line_v2)
print(three_line_str)

def test_func():
    """
    This test checks user login is successful
    """
    print("test_func")


bio = "I'm Bohdan. Im tutor of Python AQA course"
bio_2 = "I'm Bohdan. I work at 'Hillel' school"
bio_3 = """I'm Bohdan. I work at "Hillel" school"""

print(bio)
print(bio_2)
print(bio_3)

# -------------------------------------------------------
# \n - new line
ecr_1 = 'I\'m Bohdan. \nI work at "Hillel" school' # its some comment
ecr_2 = "I'am Bohdan \nI work at \"Hillel\" school"

print(ecr_1)
print(ecr_2)

new_line = '\\n is new line symbol'
tabulation = '\\t is tabulation symbol'


print(new_line)
print(tabulation)


user_id = 123456789
actual_response_status_code = 200
json_response = {
    "id": user_id,
    "status": actual_response_status_code
}

log_message = f"User with id {user_id} got status code {actual_response_status_code} \nExpected: 200 \nResponse: {json_response}"

print(log_message)
print("\t", 1)
print("    ", 1)

# -----------------------------------------------

random_string: str = "Some random string" # immutable
random_list: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 77, 99, 0, -90] # array
random_dict: dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": [1,2,3,"some_string"]
}
random_tuple: tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 77, 99, 0, -90) # list but immutable
random_set: set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 77, 99, 0, -90} # list but without indexation

len_of_random_string = len(random_string)
len_of_random_list = len(random_list)

# len is usable only for collections, sequences
print("Length of random string is: ", len_of_random_string, " symbols")
print("Length of random list is: ", len_of_random_list, " units")
print("Length of random dict is: ", len(random_dict))
print("Length of random tuple is: ", len(random_tuple), " units")
print("Length of random set is: ", len(random_set), " units")

# indexation
random_string: str = "Some random string" # [0, 1, 2, 3, 4, ...]

first_symbol = random_string[0]
second_symbol = random_string[1]
last_symbol = random_string[-1] # len(random_string) - 1
last_second_symbol = random_string[-2]


print(first_symbol, second_symbol, last_symbol, last_second_symbol)


last_3_value_from_random_list = random_list[-3]
print(last_3_value_from_random_list)


# Slices [from: to: step]
# "Some mrando string"
random_string_from_1_to_5 = random_string[:5]
random_string_from_5_to_10 = random_string[5:10]
random_string_from_10_to_end = random_string[10:]

print(random_string_from_1_to_5)
print(random_string_from_5_to_10)
print(random_string_from_10_to_end)


print(random_list[::2])

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_list_of_numbers = list_of_numbers[::-1]

slice_100_1000 = list_of_numbers[100:1000]


print(reversed_list_of_numbers)
print(slice_100_1000)

list_of_numbers[0] = 100

print(list_of_numbers)

string = "Hello, World!"
string = "Hello! World!"
print(string)


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_of_numbers[0], list_of_numbers[1] = list_of_numbers[1], list_of_numbers[0]

print(list_of_numbers)

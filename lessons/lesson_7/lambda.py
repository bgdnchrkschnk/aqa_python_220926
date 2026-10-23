def return_bio(name, age) -> str:
    return f"My name is {name} and I am {age} years old"



lambda_return_bio = lambda name, age: f"My name is {name} and I am {age} years old" if len(name) > 3 else None




# print(
#     return_bio("Donald", 75)
# )
# print(
#     lambda_return_bio("Donald", 75)
# )
#
#
# print(
#     (lambda name, age: f"My name is {name} and I am {age} years old")("Donald", 75)
# )

my_friend = ['Donald Trump', "Jeff Bezos", "Elon Musk", "Mark Zuckerberg", "Joe", "Mark"]

# -------------------------------------------------------------- filter(<func>, iterable)

# def is_friend_len_more_than_3(friend) -> bool:
#     return len(friend) > 3


my_friend_filtered: list[str] = [friend for friend in my_friend if len(friend) > 3]

my_friend_filtered_filter: filter = filter(lambda friend: len(friend) > 3, my_friend)
my_friend_filtered_tuple = tuple(my_friend_filtered_filter)


# print(my_friend_filtered_tuple)
# print(my_friend_filtered)



# ------------------------------------------- map(<func>, iterable)

my_friend_upper = [friend.upper() for friend in my_friend]
my_friend_upper_map: map = map(lambda friend: friend.upper(), my_friend)
my_friend_upper_list = list(my_friend_upper_map)

# print(my_friend_upper)
# print(my_friend_upper_list)

# -------------------------------------------- zip


my_friend_names = ["Alex", "Olga", "Mykyta", "Oleh", "Kyrylo"]
my_friend_ages = [21, 15, 28, 32, 30]
my_friend_gender = ["male", "female", "male", "female"]

zipped_friends_data: zip = zip(my_friend_names, my_friend_ages, my_friend_gender)
list_zipped_friends_data: list = list(zipped_friends_data)

# print(list_zipped_friends_data)

# --------------------------------------------- all, any

all_my_friends_name_more_4_len = all([len(friend) > 4 for friend in my_friend_names]) # [False, False, True, False, True]
any_my_friends_name_more_4_len = any([len(friend) > 4 for friend in my_friend_names])
# all -> True якщо усі елементи True
# any -> True якщо хочаб один True

# print(all_my_friends_name_more_4_len)
# print(any_my_friends_name_more_4_len)


my_friend_numbers = ["2364658", "2576357", "", None, 246890, 785763.0363]

# all(bool("2364658"), bool("2576357"), bool(""), bool(None)...]

all_my_friend_numbers = all(my_friend_numbers)
any_my_friend_numbers = any(my_friend_numbers)

# print(all_my_friends_name_more_4_len)
# print(any_my_friends_name_more_4_len)

# ------------------------------------------------------------ enumerate(iterable)


month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
index_skip = (5, 8)

for index, month in enumerate(month_names):
    if index in index_skip:
        message = f"Month index is {index}. We are not working with this month"
        # print(message)
        continue
    # print(month)


enumerated_month = list(enumerate(month_names))
# print(enumerated_month)


def build_sql_query(table: str, **condition) -> str:
    query = f"SELECT * FROM {table}"
    if condition: # {}
        query += f" WHERE"
        for index, (key, value) in enumerate(condition.items()):
            if index != 0:
                query += f" AND {key} = '{value}'"
            else:
                query += f" {key} = '{value}'"
    return query


# print(
#     build_sql_query("transactions", id=2001, status="pending", type="purchase")
# )



# ---------------------------------- callable(obj) -> bool is obj callable? ()

# print(
#     callable(month_names)
# )
#
#
# print(
#     dir(month_names)
# )


# hash("si")



class Animal:
    ...

class Dog(Animal):
    ...


dog: Dog = Dog()
animal: Animal = Animal()


# isinstance vs type

is_dog_animal = isinstance(dog, Animal) # True
is_dog_animal_type = type(dog) == Animal # Dog == Animal -> False

print(is_dog_animal)
print(is_dog_animal_type)

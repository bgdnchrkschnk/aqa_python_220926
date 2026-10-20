# MUTABLE DATA TYPE

my_bio: dict = {
    "name": "Johny",
    "age": 25,
    "hobbies": {"Programming", "Gaming", "Reading"},
    "is_married": False,
    "children": None
}

print(id(my_bio))

# VALUES - ANY type of data

# KEYS - any immutable type of data (hashable) -> hash(data)
# str, tuple, int, float, bool, None, frozenset


# dict_error = {
#     [1,2,3]: [1,2,3],
#     1: 2
# }
# ------------------------------------------- v1   dict[key]
my_bio_name: str = my_bio['name']
my_bio_hobbies: set = my_bio['hobbies']
my_bio_is_married: bool = my_bio['is_married']

# my_bio_sex: str = my_bio['sex'] - KeyError

print(my_bio_name)
print(my_bio_hobbies)
# -------------------------------------- v2   dict.get(key, default)

my_bio_name = my_bio.get("name")

# my_bio_sex: None = my_bio.get("sex") # -> None
my_bio_sex = my_bio.get("sex", "male")
print(my_bio_name)
print(my_bio_sex)


# --------------------------------------- empty dict

empty_dict = {}
empty_dict_2 = dict()

my_bio_v2: dict = dict(
    name="Johny",
    age=25,
    hobbies={"Programming", "Gaming", "Reading"},
    is_married=False,
    children=None
)

print(my_bio_v2)


# -------------------------------------- .update()

additional_bio = {
    "Favourite song": "The Weeknd - Blinding Lights",
    "Favourite movie": "The Matrix",
    "Profession": "Test Automation Engineer",
}

my_bio.update(additional_bio)

print(my_bio)
print(id(my_bio))



# --------------------------------------

keys_of_my_bio: list[str] = list(my_bio.keys())
print(type(keys_of_my_bio), keys_of_my_bio)


values_of_my_bio: list = list(my_bio.values())
print(type(values_of_my_bio), values_of_my_bio)

items_of_my_bio: list = list(my_bio.items())
print(type(items_of_my_bio), items_of_my_bio)

# -------------------------------------

for key in my_bio.keys():
    print(key)

for value in my_bio.values():
    print(value)

for key, value in my_bio.items():
    print(key, value)



string = "biehbjbnjkmnjhvuijopkwojjhb hajhfcswaerdcvbn jeuihpovrjnoijk oihreiugvfhiugui"

dict_of_letters_count: dict[str, int] = {}


for letter in string:
    if not letter.isspace():
        if not letter in dict_of_letters_count.keys():
            dict_of_letters_count[letter] = 1
        else:
            dict_of_letters_count[letter] += 1


print(dict_of_letters_count)


my_bio["age"] = 26
my_bio["new_key"] = "new_value"
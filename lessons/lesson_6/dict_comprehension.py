# dict comprehension


dict_comprehension_numbers: dict = {number: number**2 for number in range(1, 101) if number % 2 == 0}
#  {2:4, 4:16, 6:36, 8:64, 10:100}


print(type(dict_comprehension_numbers), dict_comprehension_numbers)


print(
    dict_comprehension_numbers[16], # dict[key]
    dict_comprehension_numbers.get(16),
)
# generations/filtration


payments = [
    {"id": 2343426, "status": "success", "amount": 1000},
    {"id": 2343425, "status": "failed", "amount": 8943},
    {"id": 2343466, "status": "pending", "amount": 1000},
    {"id": 2343456, "status": "success", "amount": 1000},
]

lc_filtered = [payment for payment in payments if payment["status"] == "failed"]

print(lc_filtered)

# dict comprehension

my_bio: dict = {
    "name": "Johny", # (key, value)
    "age": 25, # (key, value)
    "hobbies": {"Programming", "Gaming", "Reading"},
    "is_married": False,
    "children": None,
    "address": "",
    "phone": "",
    "friends": [],
    "email": ""
}

my_bio_filtered: dict = {key: value for key, value in my_bio.items() if bool(value)}


new_dict_filtered = {}
for key, value in my_bio_filtered.items():
    if bool(value) is True:
        new_dict_filtered[key] = value

print(my_bio_filtered)
print(new_dict_filtered)




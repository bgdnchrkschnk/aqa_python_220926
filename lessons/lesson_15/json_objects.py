import json
from pprint import pprint

from faker import Faker
from random import choice, choices, randint
from pathlib import Path
fake = Faker()

json_file = Path.cwd() / "person.json" # filepath

# l = [1,2,3]
# '-'.join(l)

person_dict: dict = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(1, 100),
    "address": fake.street_address(),
    "city": fake.city(),
    "is_married": choice([True, False]),
    "friends": [fake.name() for _ in range(randint(0, 10))],
    "phone_number": "+34" + "".join(choices(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"], k=9)),
    "additional_info": None
}

# -------------------------------- .dump() -> python dict to json file
with json_file.open("w") as json_file:
    json.dump(person_dict, json_file, indent=4)


# --------------------------------- .dumps() -> python dict to json string

json_string: str = json.dumps(person_dict)


# ---------------------------------- .load() -> json_file and convert to python dict

example_json_file = Path.cwd() / "example.json"

with example_json_file.open("r") as json_file:
    example_json_dict: dict = json.load(json_file)

    # pprint(example_json_dict)

    assert isinstance(example_json_dict, dict)
    assert example_json_dict.get("id")


# ----------------------------------- .loads() -> json_string converting to python dict

example_json_string_2 = """{
  "sku": "PRD-7741-BLK",
  "productName": "Wireless Mechanical Keyboard",
  "category": "Electronics",
  "priceUsd": 129.99,
  "inStock": true,
  "stockCount": 42,
  "tags": ["wireless", "rgb", "tactile", "usb-c"],
  "dimensionsCm": {
    "length": 31.5,
    "width": 12.7,
    "height": 3.8
  },
  "averageRating": 4.8,
  "discontinuedAt": null
}
"""

example_json_2_dict = json.loads(example_json_string_2)

assert isinstance(example_json_2_dict, dict)
assert example_json_2_dict.get("productName")

# ----------------------------------------------------


invalild_json_string = """{
  "sku": "PRD-7741-BLK",
  "productName": "Wireless Mechanical Keyboard",
  "category" "Electronics",
  "priceUsd": 129.99,
  "inStock": true
  "stockCount": 42,
  "tags": ["wireless", "rgb", "tactile", "usb-c"],
  "dimensionsCm": {
    "length": 31.5,
    "width": 12.7,
    "height": 3.8
  },
  "averageRating": 4.8,
  "discontinuedAt": null
}
"""

try:
    json.loads(invalild_json_string)
except json.decoder.JSONDecodeError:
    print(f"Invalid JSON {invalild_json_string}")

# -----------------------------
invalid_json_file = Path.cwd() / "invalid_json.json"

with invalid_json_file.open("r") as json_file:
    try:
        json.load(json_file)
    except json.decoder.JSONDecodeError:
        print(f"TEST PASS: {invalid_json_file} has not been converted to python dict!")
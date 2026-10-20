from datetime import datetime
from pprint import pprint

country = "USA"

def print_biography() -> None:
    name = "Donald"
    last_name = "Duck"
    age = 30
    biography = f"My name is {name} {last_name} and I am {age} years old. I am from {country}."
    print(biography)

# print_biography() # call
# result = print_biography()

# ------------------------------------

def return_biography() -> str:
    name = "Donald"
    last_name = "Duck"
    age = 30
    biography: str = f"My name is {name} {last_name} and I am {age} years old. I am from {country}."
    return biography

result: str = return_biography()
# print(result)


# --------------------------------------

def biography_with_params(name: str, last_name: str, age: int, return_data: bool = True) -> str | None: # default param
    biography: str = f"My name is {name} {last_name} and I am {age} years old. I am from {country}."
    if return_data:
        return biography
    print(biography)


# biography_with_params("Daniel", "Kowalski", 25, return_data=False)


michael_jackson_bio = biography_with_params("Michael", "Jackson", 30)
# print(michael_jackson_bio)


def average_result(*numbers) -> float: # free arguments input *args
    for number in numbers:
        if type(number) != int or type(number) != float:
            print("Please enter only numbers!")
            return None
    average = sum(numbers) / len(numbers)
    return average

# average_value: float = average_result(55, -90, -13, 16.7, 20, "50")


def concatenate_strings(*strings) -> str:
    return " ".join(strings)

# result_string: str = concatenate_strings("Hello", "", "World!", "I", "am", "a", "string")


def describe_person(name: str, age: int, **extra_data) -> str:
    bio = f"My name is {name} and I am {age} years old."
    print(type(extra_data), extra_data)
    if extra_data: # {}
        extra_data_str = "Extra data: "
        for key, value in extra_data.items():
            extra_data_str += f"{key}: {value}, "
        bio += extra_data_str
    return bio

bio = describe_person("John", 25, country="USA", city="New York", favorite_food="Pizza")
print(bio)

def make_cv(*skills, **candidate_info) -> dict:
    cv = {
        "candidate_info": candidate_info,
        "skills": list(skills),
        "timestamp": datetime.now(),
        "company_name": "Python Academy"
    }
    return cv


my_cv: dict = make_cv("Python", "API", "Pytest", "SQL", name="Oleg", age=25, country="Ukraine", city="Kyiv", experience="5 years")
pprint(my_cv)
from traceback import print_tb

from lessons.lesson_3.bool_alg import age

print(bool([])) # False
print(bool([1, 2, 3])) # True
print(bool("Some string")) # True
print(bool("")) # False
print(bool(" ")) # True
print(bool(None)) # False
print(bool(True)) # True
print(bool(False)) # False
print(bool(23)) # True
print(bool(-2)) # True
print(bool(0.0)) # False
print(bool(0.000000000001)) # True
print(bool({})) # False
print(bool(set())) # False
print(bool([[], [], []])) # True


# bool(False) vs bool(None)

my_bio: dict = {
    "name": "Johny",
    "age": 25,
    "hobbies": {"Programming", "Gaming", "Reading"},
    "is_married": False,
    "children": None
}


if my_bio.get("age"): # bool(age)
    print("User age is not empty")

if my_bio.get("name"):
    print("User name is not empty")

if my_bio.get("hobbies"):
    print("User hobbies is not empty")


if not my_bio.get("hobbies"):
    print("User hobbies is empty")

if my_bio.get("is_married") is None:
    print("User is not married")

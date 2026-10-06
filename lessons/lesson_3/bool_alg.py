"""
True and True -> True
True and False -> False

True or True -> True
False or True -> True
False or False -> False


not True -> False
not False -> True
"""

username: str = "admin"
email: str = ""
password: str = "Qwerty!"
age: int = 18
is_legal: bool = False


print(bool([]))
print(bool([1, 2, 3]))
print(bool("Some string"))
print(bool(""))
print(bool(" "))
print(bool(None))
print(bool(True))
print(bool(False))
print(bool(23))
print(bool(-2))
print(bool(0))

# if condition
if bool(username) and bool(password) and bool(is_legal):
    print(f"User {username} is registered!")
if not bool(password):
    print("Password is empty!")
if not bool(is_legal):
    print("User is not legal!")

if username and password and is_legal:
    print(f"User {username} is registered!")
if not password:
    print("Password is empty!")
if not is_legal:
    print("User is not legal!")
if email:
    print("Saving email to database...")

if is_legal or age >= 18:
    print("User is legal!")

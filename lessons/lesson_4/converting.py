number: int = 5000
number_fl: float = 5000.0

number_str = str(number)
number_fl_str = str(number_fl)

print(number_str, type(number_str))
print(number_fl_str, type(number_fl_str))

print(str([63, "ebsjbf", True]))

# ----------------------------------------

number_str = "50000"

number: int = int(number_str)
number_fl: float = float(number_str)

print(number, type(number))
print(number_fl, type(number_fl))


# ----------------------------------

print(
    bool(True) # True
)

print(
    bool(False) # False
)

print(
    bool("True") # True
)

print(
    bool("False") # True
)


text = " Hello, World!"

list_text: list[str] = list(text)
tuple_text: tuple[str] = tuple(text)
set_text: set[str] = set(text)

print(list_text)
print(tuple_text)
print(set_text)
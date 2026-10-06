from decimal import Decimal

"""
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
"""


# def = "some text" ! Wrong

some_var: None = None

assert bool(15 == 15) # bool()   # assert True/False


my_age = 19
club_access = 18

print(my_age < club_access) # False
print(my_age > club_access) # True
print(my_age == club_access)
print(my_age >= club_access)
print(my_age <= club_access)
print(my_age != club_access) # True

print(not my_age == club_access)

"""
+       -       *       **      /       //      %
"""

print("+", 10 + 3)
print("-", 10 - 3)
print("*", 10 * 3)
print("**", 10 ** 3)
print("/", 10 / 2) # float (неціле число)
print("//", 10 // 3) # int (ціле число) 3 int(3.33)
print("%", 10 % 3) # 1

integer_digit: int = 10
float_digit: float = 10.5

a = 0.1
b = 0.2

# assert a + b == 0.3, f"{a+b}"

a = Decimal("0.1")
b = Decimal("0.2")
assert a + b == Decimal("0.3"), f"{a+b}"

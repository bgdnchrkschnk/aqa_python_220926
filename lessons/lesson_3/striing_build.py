username: str = "admin"
email: str = ""
password: str = "Qwerty!"
age: int = 18
is_legal: bool = False


bio_fstring = f"My name is {username} and I am {age} years old. I am {is_legal} legal. My email is {email}"
bio_format = "My name is {} and I am {} years old. I am {} legal. My email is {}".format(username, age, is_legal, email)
bio_format_v2 = "My name is {username} and I am {age} years old. I am {is_legal} legal. My email is {email}".format(username=username, age=age, is_legal=is_legal, email=email)


print(bio_fstring)
print(bio_format)
print(bio_format_v2)

print(f"My name is {username} and I am {10+8} years old. I am {is_legal} legal. My email is {email}.")


age = input("How old are you? ")


print(f"Your age is {age}")


"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

monthly_bill: float = 1179
total_cost = monthly_bill * 12
print(f"Total cost of the computer is {total_cost} UAH")
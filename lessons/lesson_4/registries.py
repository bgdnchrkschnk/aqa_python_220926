message = "WeLCoMe, oLeG! YOur baLAncE iS 400 USd"


welcome_message_lower = message.lower()
welcome_message_upper = message.upper()
welcome_message_title = message.title()
welcome_message_capitalize = message.capitalize()


# print(welcome_message_lower)
# print(welcome_message_upper)
# print(welcome_message_title)
# print(welcome_message_capitalize)

if "USD" in message.upper():
    print("$ balance is detected!")
if "EUR" in message.upper():
    print("€ balance is detected!")
message = message.title()


print(message)

# -------------------------------------------

is_message_upper: bool = message.isupper() # All letters are upper case
is_message_title: bool = message.istitle() # First letter is upper case, others are lower case
is_message_lower: bool = message.islower() # All letters are lower case
is_message_digit: bool = message.isdigit() # All letters are digits
is_message_alnum: bool = message.isalnum() # All letters are digits or letters
is_message_space: bool = message.isspace() # All letters are space


telephone_number = "1234-5-67890"

if telephone_number.isdigit():
    telephone_number = int(telephone_number)
    print("telephone number is digit. saved as int in db: ", telephone_number)
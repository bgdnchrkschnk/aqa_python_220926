import time
from random import randint

# while <condition>

# while True:
#     print("Hello")

while False:
    print("Hello")

if False:
    print("Hello")

# number = 0
# limit = 15
# while number <= limit:
#     print("The number is: ", number)
#     # number = number + 1
#     number += 1
# print(number)


# my_age = 13
# entry_age = 18
#
# while my_age < entry_age:
#     print(f"You are still young ({my_age}) to become AQA enginer. We are welcome you. when you become {entry_age}")
#     time.sleep(1)
#     my_age += 1
# else:
#     print("Welcome to AQA!")


secret_number = randint(1,10)

while True:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Secret number is: ", secret_number, "You are right!")
        break
    else:
        print("You are wrong! Try again.")




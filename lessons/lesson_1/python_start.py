

# text: str = "Hello, World!"
# name: str = "Joseph"
#
# # print(text, name)
#
# five_is_five: bool = 5 == "5"
#
# print(five_is_five)
#
# # five_is_five # snake case
# # myBirthdayDate # camel case
#
#
# my_birthday_date: str = "1990-01-01"
#
# # ------------------------------------------
#
# a = "pesyk"
# b = 12
# c = True

my_dog_name = "Pesyk"
my_dog_age = 5
my_dog_is_healthy = True
my_dog_birthday_date: str = "2010-01-01"

if my_dog_is_healthy is False:
    print("My dog is not healthy! Giving some rest!")

    if my_dog_age > 10:
        print("Giving my dog some drugs!")

a = 5
b = 10
c = 15
d = 50

sum_numbers: int = a + b + c + d
diff_numbers: int = d - c - b - a
multiply_numbers: int = a * b * c * d
divide_numbers: float = d / c / b / a


print(sum_numbers, diff_numbers, multiply_numbers, divide_numbers, sep="\n", end="\nALL NUMBERS CALCULATED!")


# print(sum_numbers)
# print(diff_numbers)
# print(multiply_numbers)
# print(divide_numbers)

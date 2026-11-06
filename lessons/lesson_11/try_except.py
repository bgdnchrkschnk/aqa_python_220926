def divide(a, b):
    return a / b

test_data = [
    (5,2),
    (3,5),
    (10,0),
    ("15", 2),
    (5,1),
    (2,7),
]

# a, b = (5, 2)

# try except else finally

# for a, b in test_data:
#     try:
#         result = divide(a,b)
#         print(result)
#     except (ZeroDivisionError, TypeError) as error:
#         print(f"{error}: {a}, {b}")


# for a, b in test_data:
#     try:
#         result = divide(a,b)
#         print(result)
#     except Exception as error:
#         ...

#
# try:
#     for a, b in test_data:
#         result = divide(a,b)
#         print(result)
# except (ZeroDivisionError, TypeError) as error:
#     ...
# finally:
#     print(f"Script ended")
# db_connection = None
# try:
#     db_connection = psycopg.connect(**config) # Connection error
#     cursor = db_connection.cursor()
#
#     cursor.execute("SELECT * FROM users")
# except Exception as error:
#     print(f"Something went wrong. {error}")
# finally: # він виконується завжди незалежно від того чи було падіння помилки
#     if db_connection:
#         db_connection.close()



def is_adult(age: int) -> bool:
    return age >= 18

list_of_ages = [18, 25, 35, 0, -65, 70, 80]

try:
    for age in list_of_ages:
        message = f"Age {age} is adult: {is_adult(age)}"
        print(message)
except:
    ...
else: # якщо не сталось падінь помилок (else завжди після except)
    print("Send success mail!")
finally:
    print("Finally finished process")
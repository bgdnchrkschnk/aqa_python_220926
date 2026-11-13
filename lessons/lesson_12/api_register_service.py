from helpers.helpers import assert_logged
from lessons.lesson_13.custom_logger import custom_logger

REGISTERED_USERS = []

class APIRegisterDuplicateException(Exception):
    """
    Exception for duplicate users attempt
    """


def register(username: str, password: str, email: str, phone_number: str):
    """
    User registration form endpoint
    """
    custom_logger.info(f"Trying to register (user {username}, phone number {phone_number}, email {email})")
    if email.count("@") != 1: # <str> not in <str>  @ not in email, @ more than 1 count
        custom_logger.error(f"Email address {email} is invalid!")
        return {"status_code": 400, "error_msg": "email field validation error"}
    if len(password) < 8 or (password == password.lower()):
        custom_logger.error(f"User password {password} is invalid!")
        return {"status_code": 400, "error_msg": "password is not secure"}
    if not phone_number.isdigit():
        custom_logger.error(f"User phone {phone_number} is invalid!")
        return {"status_code": 400, "error_msg": "phone number is invalid"}
    user = {"username": username, "phone_number": phone_number, "email": email}

    assert_logged(condition=user in REGISTERED_USERS, msg=f"User {user} is already registered!", exception=APIRegisterDuplicateException)

    REGISTERED_USERS.append(user)
    custom_logger.info(f"Successfully registered user {user}")
    return {
        "status_code": 200,
        "user": user
    }




# if __name__ == "__main__":
#     # print(
#     #     register(username="Christiano_Ronaldo", password="bhjsbefhhG", email="chrisronaldo@gmail.com", phone_number="67567514274")
#     # )
#     # print(
#     #     register(username="Oleksandr", password="Usykefjkbjw", email="usyk357@gmail.com", phone_number="3665675673"))
#     # print(REGISTERED_USERS)
#     print(f"sys.path: {sys.path}")
#     import outside
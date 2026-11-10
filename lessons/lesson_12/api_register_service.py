
REGISTERED_USERS = []

class APIRegisterDuplicateException(Exception):
    """
    Exception for duplicate users attempt
    """


def register(username: str, password: str, email: str, phone_number: str):
    """
    User registration form endpoint
    """
    print(f"[API_REGISTER] Trying to register (user {username}, phone number {phone_number}, email {email})")
    if email.count("@") != 1: # <str> not in <str>  @ not in email, @ more than 1 count
        return {"status_code": 400, "error_msg": "email field validation error"}
    if len(password) < 8 or (password == password.lower()):
        return {"status_code": 400, "error_msg": "password is not secure"}
    if not phone_number.isdigit():
        return {"status_code": 400, "error_msg": "phone number is invalid"}
    user = {"username": username, "phone_number": phone_number, "email": email}

    if user in REGISTERED_USERS:
        raise APIRegisterDuplicateException

    REGISTERED_USERS.append(user)
    print(f"[API_REGISTER] Registered user {username}")
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
from exceptions.lesson_11 import IsAdultFuncError


def is_adult(age: int | float) -> bool:
    if type(age) not in (int, float):
        raise IsAdultFuncError(f"age can't be type {type(age)}") # викинути помилку
    return age >= 18



try:
    # print(is_adult("jnkjsefes"))
    raise IsAdultFuncError
except IsAdultFuncError:
    ...
else:
    print("No errors")
finally:
    print("finally")
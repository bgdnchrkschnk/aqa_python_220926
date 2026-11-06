# LEGB ( Local - Enclosing - Global - Built-it )


str = "Global"

def outer():

    str = "Nonlocal" # enclosing

    def inner():
        global str # call
        str = "Local"

    inner()

outer()
print(str)
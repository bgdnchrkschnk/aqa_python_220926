from typing import Any


class User:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.friends = []
        self.is_married = False

    def __str__(self) -> str: # for user
        return f"Instance of User class: {self.__dict__}, id:{id(self)}"

    def __repr__(self) -> str: # technical representation (terminal debugging, console)
        return f"User(name={self.name}, age={self.age}, gender={self.gender})"

    def __len__(self):
        return len(self.name)

    def __gt__(self, other_user): # >
        return self.age > other_user.age

    def __lt__(self, other_user):
        return self.age < other_user.age

    def __eq__(self, other_user) -> bool:
        return self.__dict__ == other_user.__dict__

    def __add__(self, other_user) -> None:
        """
        The function adding friend to a list of friends
        """
        # self.friends.append(other_user)
        # other_user.friends.append(self)
        if self.is_married or other_user.is_married:
            print(f"Some of these users are already married")
            return
        self.is_married = True
        self.partner = other_user

        other_user.is_married = True
        other_user.partner = self

    def __getattribute__(self, item):
        print(f"Reading {item}")
        return super().__getattribute__(item)

    def __getattr__(self, item): # not existing attr
        print(f"Getting {item}")

    def __setattr__(self, key, value):
        if key == "is_married" and getattr(self, "is_married") is not None:
            print(f"Setting {key} is not supported now!")
            return
        if key == "gender" and value not in ["male", "female"]:
            print(f'Only ["male", "female"] are available to set!')
            return
        return super().__setattr__(key, value)

    def __delattr__(self, item):
        print(f"Deleting {item}")
        return super().__delattr__(item)

    def __del__(self): # garbage collector
        print(f"Deleting {self}")

if __name__ == '__main__':
    michael: User = User("Michael", 18, "m")
    simona: User = User("Simona", 22, "f")
    #
    # print(michael) # __str__
    # # print(simona)
    #
    # # print(repr(michael))
    # # print(repr(simona)) # REPL
    #
    #
    # len_simona = len(simona)   # 6 len
    # len_michael = len(michael) # 7 len
    #
    # is_michael_bigger_than_simona: bool = michael > simona
    # is_michael_younger_than_simona: bool = michael < simona
    #
    # michael_copy = michael # id той самий обʼєкта
    # User("Michael", 18, "m")
    #
    #
    # michael_fake = User("Michael", 18, "m") # new id object
    #
    # michael_copy_is_equal_michael: bool = michael == michael_copy # True
    # michael_fake_is_equal_michael: bool = michael == michael_fake # False
    # michael_fake_is_equal_michael_copy : bool = michael_fake == michael_copy # False
    #
    #
    # michael + simona
    #
    # print(simona.friends)



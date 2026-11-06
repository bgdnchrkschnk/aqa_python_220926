# INHERITANCE
# Polymorphism



class Animal:
    def __init__(self, name: str):
        self.name = name

    def move(self):
        if type(self) is Dog:
            print(f"Dog is moving...")
        elif type(self) is Cat:
            print(f"Cat is moving...")
        elif type(self) is MiniDog:
            print(f"MiniDog is moving...")

class Dog(Animal):
    def __init__(self, name: str, breed: str, age: int):
        super().__init__(name) # Animal init
        self.breed = breed
        self.age = age

    # def move(self):
    #     print(f"Dog is moving...")

class Cat(Animal):
    def __init__(self, name: str, date_of_birth: str, character: str):
        super().__init__(name)
        self.date_of_birth = date_of_birth
        self.character = character

    # def move(self):
    #     print(f"Cat is moving...")

class MiniDog(Dog):
    def __init__(self, name: str, breed: str, age: int, weight: int):
        super().__init__(name, breed, age)
        self.weight = weight

    # def move(self):
    #     print(f"MiniDog is moving...")


dog = Dog(name="Doggie", breed="Dog", age=18)
cat = Cat(name="Cattie", date_of_birth="07.10.2025", character="soft")
minidog = MiniDog(name="Tuzik", breed="chihua", age=1, weight=2)


# animals = [dog, cat, minidog]
#
# for animal in animals:
#     animal.move()

def make_it_move(obj):
    obj.move()

# make_it_move(dog)
# make_it_move(cat)
# make_it_move(minidog)


# INCAPSULATION
# public
# protected
# private




class BankAccount:
    def __init__(self, name: str, account_type: str, balance: int):
        self.name = name # public
        # self.account_type = account_type # public
        # self.balance = balance # public
        self._account_type = account_type # protected ( '_' - говорить про те що це технічний атрибут)
        # self._balance = balance # protected
        self.__balance = balance # private (mangling name)

        self.__creating_cell_in_db() # start creating bank account...


    def __creating_cell_in_db(self): # private
        # db_client.insert_record_in_table
        # db_client.creating_audit_account
        ...

    def get_my_balance(self) -> int:
        return self.__balance






bank_account = BankAccount("Oleg", "classic", 100)
# print(
#     bank_account.get_my_balance()
# )


print(bank_account._BankAccount__balance) # mangling mechanism

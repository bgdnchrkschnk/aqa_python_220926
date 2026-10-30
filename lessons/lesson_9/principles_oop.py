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

make_it_move(dog)
make_it_move(cat)
make_it_move(minidog)


class Animal:
    eyes = 2
    tail = 1
    head = 1

    def move(self):
        print('moving...')

    def eat(self):
        print('Animal is eating')

    def sleep(self):
        print('Animal is sleeping')

    def make_sound(self):
        print('Animal is making sound')


class Dog(Animal):
    def make_sound(self):
        print(f"WOOF!")

class Cat(Animal):
   def make_sound(self):
       print(f"MEOW!")

animal = Animal()
dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()

# при наслідуванні клас наслідник отримує всі характеристики та поведінку від батьківського
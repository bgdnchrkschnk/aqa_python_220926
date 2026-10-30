from typing import Self


class User:
    def __init__(self, name, age): # initialization
        self.name = name
        self.age = age

    def say(self, message="Hello"):
        print(f"{self.name} says: {message}")

    def __del__(self): # magic methods (double underscore method)
        print(f"{id(self)} is deleted")

# Initialization (construction)
volodya = User("Volodya", 20) # id
mykhailo = User("Mykhailo", 30) # id


# Utilization of the object (using)

volodya.gender = "male"
mykhailo.favourite_music_genre = "Hip-Hop"

mykhailo.favourite_music_genre = "Pop"

print(volodya.name)
print(mykhailo.favourite_music_genre)


mykhailo.say()
volodya.say("Goodbye! I'll be back!")

# Destruction of the object (Deleting object in memory)

# garbage collector

del volodya # не видаляє обʼєкт в памяті (видаляє лише посилання на цей обʼєкт)


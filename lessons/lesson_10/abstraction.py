from abc import ABC, abstractmethod

# ABSTRATION

# клас називається абстрактним якщо в нього хоча б 1 абстрактний метод
# абстрактний клас не ініціалізується
class Animal(ABC):

    @abstractmethod
    def eat(self):
        print("Eating")

    @abstractmethod
    def sleep(self):
        print("Sleeping")

    def make_sound(self):
        print("Making sound")

class Dog(Animal):

    def sleep(self):
        print("Dog Sleeping")

    def eat(self):
        print("Dog is eating...")

class Cat(Animal):

    def scratch(self):
        print("Cat scratch")

    def sleep(self):
        print("Cat sleep")


dog = Dog()
dog.make_sound()

# .....................................................


class AbstractDBClient(ABC):

    @abstractmethod
    def __connect(self, host, port , dbname, user, password):
        ...

    @abstractmethod
    def reset_database(self):
        ...

    @abstractmethod
    def close_connection(self):
        ...

class PostgresClientPROD(AbstractDBClient):

    def __connect(self, host, port, dbname, user, password):
        ...
        # psycopg.connection...

    def reset_database(self):
        ...
        # psycopg.reset()

    def close_connection(self):
        ...
        # self.connection.cursor.close()

class SQLLiteDEV(AbstractDBClient):

    def __connect(self, host, port, dbname, user, password):
        ...
        # sqlite.connect(host, port, dbname, user, password)

    def reset_database(self):
        ...
        # sqlite.reset()

    def close_connection(self):
        ...
        # self.connection.connection.close()

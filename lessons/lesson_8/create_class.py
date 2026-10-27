

# АТРИБУТИ (атрибути класу, методи)

# (характеристика та поведінка)
# (атрибути, функції)


class Car: # MyFavouriteCar ->  my_favourite_car
    wheels = 4
    engine = 1

    def drive_to(self, destination: str) -> None:
        print(f"Driving to {destination}...")


my_car: Car = Car() # -> instance of the class (екземпляр класу)
my_car_2: Car = Car()
my_car_3: Car = Car()


# for car in [my_car, my_car_2, my_car_3]:
#     print(id(car))

my_car.drive_to(destination="New York")
my_car_2.drive_to(destination="Los Angeles")
my_car_3.drive_to(destination="California")

print(my_car.wheels, my_car.engine)
print(my_car_2.wheels, my_car_2.engine)
print(my_car_3.wheels, my_car_3.engine)


class SportsMan:
    ...
    # pass

klitchko = SportsMan()

class DiveMixin:
    def try_dive(self):
        print("Trying dive...")


class Transport:
    def __init__(self, engine: bool, max_speed: int, capacity: int):
        self.engine = engine
        self.max_speed = max_speed
        self.capacity = capacity

    def drive(self):
        print("Some transport is driving...")

class LandTransport(Transport):
    def __init__(self, land_wheels, **kwargs):
        super().__init__(**kwargs)
        self.land_wheels = land_wheels

    def drive(self):
        super().drive()
        print("Driving on a land...")


    def honk(self):
        print("Land transport is honking...")


class WaterTransport(Transport):
    def __init__(self, sail: bool, **kwargs):
        super().__init__(**kwargs)
        self.sail = sail

    def drive(self):
        super().drive()
        print("Swimming on a water...")

    def honk(self):
        print("Water transport is honking...")


class AirTransport(Transport):
    def __init__(self, wings: str, **kwargs):
        super().__init__(**kwargs)
        self.wings = wings

    def drive(self):
        super().drive()
        print("Flying on a air...")

    def honk(self):
        print("Flying transport is honking...")


class AmphibiousTransport(LandTransport, WaterTransport):
    def __init__(self, amphibious_model, **kwargs):
        super().__init__(**kwargs)
        self.amphibious_model = amphibious_model

    def drive(self):
        super().drive()

class AirWaterTransport(AirTransport, WaterTransport):
    def __init__(self, air_water_model, **kwargs):
        super().__init__(**kwargs)
        self.air_water_model = air_water_model

    def drive(self):
        super().drive()

class HybridTransport(AmphibiousTransport, AirWaterTransport, DiveMixin):
    def __init__(self, hybrid_model, is_licensed, **kwargs):
        super().__init__(**kwargs)
        self.hybrid_model = hybrid_model
        self.is_licensed = is_licensed

    def drive(self):
        super().drive()



land_transport = LandTransport(land_wheels=4, engine=True, max_speed=150, capacity=6)
water_transport = WaterTransport(sail=True, engine=True, max_speed=150, capacity=6)
print(
    land_transport.__dict__
)
print(
    water_transport.__dict__
)

amphibious_transport = AmphibiousTransport(amphibious_model=1.2, engine=True, max_speed=150, capacity=6, sail=True, land_wheels=4)
amphibious_transport.drive()


# print(isinstance(amphibious_transport, AmphibiousTransport))
# print(isinstance(land_transport, LandTransport))
# print(isinstance(water_transport, WaterTransport))
# print(isinstance(land_transport, Transport))

tesla: HybridTransport = HybridTransport(
    hybrid_model=3.0,
    air_water_model=1.0,
    amphibious_model=1.0,
    is_licensed=True,
    engine=True,
    max_speed=370,
    capacity=5,
    sail=False,
    land_wheels=4,
    wings=0,
)


print(all([
    isinstance(tesla, Transport),
    isinstance(tesla, LandTransport),
    isinstance(tesla, WaterTransport),
    isinstance(tesla, AirTransport),
    isinstance(tesla, AmphibiousTransport),
    isinstance(tesla, HybridTransport),
    isinstance(tesla, AirWaterTransport)
]))

print(any([
    hasattr(tesla, "engine"),
    hasattr(tesla, "max_speed"),
    hasattr(tesla, "capacity"),
    hasattr(tesla, "sail"),
    hasattr(tesla, "land_wheels"),
    hasattr(tesla, "wings"),
    hasattr(tesla, "is_licensed")
    ])
)

tesla.try_dive()
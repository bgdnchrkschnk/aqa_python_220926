

class Car:
    wheels = 4
    engine = 1

    def __init__(self, model_param: str, v_engine_param: float | int, date_of_purchase_param: str, tank_param=30):
        self.model = model_param
        self.v_engine = v_engine_param
        self.date_of_purchase = date_of_purchase_param
        self.tank = tank_param
        self.usage_gas = 0.5

    def drive_to(self, destination: str, km: int) -> None:
        gas_required = km * self.usage_gas

        if gas_required > self.tank:
            print(f"[{self.model}], Not enough gas to drive to {destination}. Need additional {abs(self.tank - gas_required)} l")
            return
        print(f"[{self.model}] Driving to {destination}... Estimated gas usage: {gas_required} l")
        self.tank -= gas_required
        print(f"[{self.model}] Tank remaining {self.tank} l")

#
# toyota_camry: Car = Car("Toyota Camry", 3.5, "02.03.2026")
# porsche_911: Car = Car("Porsche 911", 5, "16.04.2025", tank_param=25)
#
#
# toyota_camry_date_of_purchase = toyota_camry.date_of_purchase
# porsche_911_v_engine = porsche_911.v_engine
#
# print(toyota_camry_date_of_purchase)
# print(porsche_911_v_engine)
#
#
# toyota_camry.color = "red"
# toyota_camry.color = "green"
# # print(toyota_camry.color)
#
#
# porsche_911.drive_to("Kyiv", 20)
# porsche_911.drive_to("Bucha", 14)
# # toyota_camry.drive_to("Budapest", 300)
#
#
# # print(toyota_camry.tank)
#
# porsche_911.tank = 100
#
# print(porsche_911.tank)

porsche_911: Car = Car("Porsche 911", 5, "16.04.2025", tank_param=25)

porsche_911.drive_to("Ternopil", 200)
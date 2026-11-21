class transport():
    def __init__(self, name):
        self.name = name
    def road(self):
        print(f"{self.name} run on roads")
        

class petrol(transport):
    def normal(self):
        print(f"{self.name} runs on normal fuel")
    def E20(self):
        print(f"{self.name} runs on E20 fuel")

class diesel(transport):
    def heavy(self):
        print(f"{self.name} runs on diesel")


class bike(petrol):
    pass

class bus(diesel):
    pass

class vehicle(petrol, diesel):
    pass


pulsar = bike("Pulsar")
pulsar.E20()
pulsar.road()

car = vehicle("Verna")
car.normal()
car.heavy()
# Composition = Just like aggregation but the classes are not idependent of each other. Has owning relationship.

class Processor:
    def __init__(self, name):
        self.name = name

class Display:
    def __init__(self, size):
        self.size = size

class Mobile:
    def __init__(self, Brand, Model, CPU, Display_Unit ):
        self.Brand = Brand
        self.Model = Model
        self.cpu = Processor(CPU)
        self.screen = Display(Display_Unit)
    def specify(self):
        return f"{self.Brand} {self.Model} {self.cpu.name} {self.screen.size}"

Mobile1 = Mobile(Brand="Samsung Galaxy", Model="A16", CPU="Snapdragon 605", Display_Unit="IPS_LCD")

print(Mobile1.specify())
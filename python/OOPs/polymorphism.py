from abc import ABC, abstractmethod

class Shapes(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius**2

class Square(Shapes):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side**2

class Parallelogram(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base*self.height


shapes = [Circle(98), Square(40), Parallelogram(20, 15)]

for shape in shapes:
    print(f"The area of {shape} is {shape.area()}")
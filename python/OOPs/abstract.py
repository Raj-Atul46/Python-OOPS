from abc import ABC, abstractmethod

class milk(ABC):
    pass

    @abstractmethod
    def milkratio():
        pass

    @abstractmethod
    def sweetner():
        pass

class milk_coffee(milk):
    def milkratio(self):
        print("Your Milk ratio will depend upon the type.")
    def sweetner(self):
        print("You can add the sweetner.")

cappuccino = milk_coffee()

cappuccino.milkratio()

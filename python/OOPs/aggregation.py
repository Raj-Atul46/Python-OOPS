#Aggregation = It is like a cotainer thing that have independent objects in it. The thing is that both are independent of each other.

class Grocery_Store:
    def __init__(self, name):
        self.name = name
        self.veggies = []

    def add_Veg(self, veg):
        self.veggies.append(veg)

    def list_Veg(self):
        return [f"{veg.name}" for veg in self.veggies]

class vegetables:
    def __init__(self, name, is_imported):
        self.name = name
        self.is_imported = is_imported

grocery_store = Grocery_Store("The Scorp Store")

veg1 = vegetables("Cauliflower", False)
veg2 = vegetables("Broccoli", True)
veg3 = vegetables("Potato", False)

grocery_store.add_Veg(veg1)
grocery_store.add_Veg(veg2)
grocery_store.add_Veg(veg3)

print(grocery_store.name)
for veg in grocery_store.list_Veg():
    print(veg)

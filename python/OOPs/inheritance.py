class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    pass

class Cat(Animal):
    pass


dog = Dog("Tommy", "Has four legs")
cat = Cat("Mimy", "Has four short legs")

print(dog.name)
print(dog.legs) 
dog.eat() 
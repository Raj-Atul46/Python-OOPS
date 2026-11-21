class Electronics:
    def __init__(self, material, camera):
        self.material = material
        self.camera = camera

    def describe(self):
        print(f"It is a phone made of {self.material} having {'front and back camera' if self.material is "Polycarbonate" else 'HD camera'}")


class Phone(Electronics):
    def __init__(self, material, color, network, camera):
        super().__init__(material, camera)
        self.color = color
        self.network = network

    def describe(self):
        super().describe()
        print(F"{self.material} is strong and looks stylish.")

class Laptop(Electronics):
    def __init__(self, material, color, has_gpu, camera):
        super().__init__(material, camera)
        self.color = color
        self.has_gpu = has_gpu

class Desktop(Electronics):
    def __init__(self, material, has_gpu, camera):
        super().__init__(material, camera)
        self.has_gpu = has_gpu


mobile = Phone(material="Polycarbonate", camera="108 MegaPixels", color="Blue", network="5G")
asus = Laptop(material="Metal", color="Grey", has_gpu=True, camera="Yes")

mobile.describe()
asus.describe()
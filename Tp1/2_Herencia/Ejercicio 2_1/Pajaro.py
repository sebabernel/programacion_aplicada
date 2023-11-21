from Animal import Animal

class Pajaro(Animal):
    def __init__(self, nombre, edad, especie):
        super().__init__(nombre, edad)
        self._especie = especie

    def cantar(self):
        print("¡Pio!")

    def hablar(self):
        print("¡¡¡Pio... Pio!!!")
        
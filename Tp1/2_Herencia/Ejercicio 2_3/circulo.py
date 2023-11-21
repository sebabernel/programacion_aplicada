from forma import Forma

class Circulo(Forma):
    def __init__(self, color, radio):
        super().__init__(color, dimensiones = None)
        self.radio = radio
        self.dimensiones = None

    def calcular_area(self):
        return 3.14 * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.14 + self.radio



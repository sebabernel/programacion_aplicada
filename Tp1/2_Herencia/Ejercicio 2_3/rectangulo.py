from forma import Forma

class Rectangulo(Forma):

    def __init__(self, color, base, altura):
        super().__init__(color, dimensiones = None)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (2 * (self.base + self.altura))
from Figura_Geometrica import Figura_Geometrica

class Circulo(Figura_Geometrica):
    PI = 3.1459
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio
    
    def calcular_area(self):
        return self.PI * self._radio ** 2
    
    def calcular_perimetro(self):
        return 2 * self.PI * self._radio
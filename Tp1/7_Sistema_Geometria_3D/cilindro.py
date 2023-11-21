import math
from figura3D import Figura3D

class Cilindro(Figura3D):

    def __init__(self, punto, radio, altura):
        super().__init__()
        self._punto = punto
        self._radio = radio
        self._altura = altura
    
    def calcular_volumen(self):
        return math.pi * self._radio * (self._radio + self._altura)

    def calcular_area_superficial(self):
        return 2 * math.pi * self._radio * (self._radio + self._altura)
    
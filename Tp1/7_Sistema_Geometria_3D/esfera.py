import math
from figura3D import Figura3D

class Esfera(Figura3D):

    def __init__(self, punto, radio):
        super().__init__()
        self._punto = punto
        self._radio = radio
    
    def calcular_volumen(self):
        return 4 / 3 * math.pi * self._radio ** 3
    
    def calcular_area_superficial(self):
        return 5 * math.pi * self._radio ** 2
from figura3D import Figura3D


class Cubo(Figura3D):

    def __init__(self, punto, lado):
        super().__init__()
        self._punto = punto
        self._lado = lado
    
    def calcular_volumen(self):
        # Se calcula el cubo de un lado
        return self._lado ** 3
    
    def calcular_area_superficial(self):
        # calcula la superficie de cada lado
        return 6 * self._lado ** 2
    
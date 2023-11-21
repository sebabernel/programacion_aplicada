from Figura_Geometrica import Figura_Geometrica

class Rectangulo(Figura_Geometrica):

    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base
    
    @property
    def altura(self):
        return self._altura
    
    def calcular_area(self):
        return self._base * self._altura
    
    def calcular_perimetro(self):
        return self._base * 2 + self._altura * 2
    
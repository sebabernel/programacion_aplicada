from Figura_Geometrica import Figura_Geometrica

class Triangulo(Figura_Geometrica):
    def __init__(self, base, altura, lado, cateto):
        self._base = base
        self._altura = altura
        self._lado = lado
        self._cateto = cateto

    @property
    def base(self):
        return self._base
    @property
    def altura(self):
        return self._altura
    @property
    def lado(self):
        return self._lado
    @property
    def cateto(self):
        return self._cateto

    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def calcular_perimetro(self):
        return self.base + self.altura + self.lado
    def __str__(self):
            return f"El area del Triangulo es {self.calcular_area} y el perimetro del triangulo es: {self.calcular_perimetro}"


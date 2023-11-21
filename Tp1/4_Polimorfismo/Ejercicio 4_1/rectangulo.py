from figura_geometrica import Figura_Geometrica

class Rectangulo(Figura_Geometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        super().__init__(base * altura, 2 * base * + 2 * altura)
        
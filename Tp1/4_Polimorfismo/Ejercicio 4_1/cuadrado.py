from figura_geometrica import Figura_Geometrica

class Cuadrado(Figura_Geometrica):
    def __init__(self, lado):
        self.lado = lado
        super().__init__(lado * lado, 4 * lado)
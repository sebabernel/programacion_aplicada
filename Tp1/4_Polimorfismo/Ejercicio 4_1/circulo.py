from figura_geometrica import Figura_Geometrica

class Circulo(Figura_Geometrica):
    def __init__(self, radio):
        self.radio = radio
        
        super().__init__(3.1416 * radio ** 2, 2 * 3.1416 * radio)

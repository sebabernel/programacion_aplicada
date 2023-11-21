from Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    
    def __init__(self, marca, modelo, velocidad_maxima, tipo):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo = tipo

    def pedalear(self):
        print("Pedalea mas rapido")
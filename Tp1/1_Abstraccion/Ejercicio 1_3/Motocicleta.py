from Vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, cilindrada):
        super().__init__(marca, modelo, velocidad_maxima)
        self.cilindrada = cilindrada
        self.tipo = "Motocicleta"
        
    def inclinarse(self):
        print("La motocicleta se esta inclinando")
from Vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, numero_puertas):
        super().__init__(marca, modelo, velocidad_maxima)
        self.numero_puertas = numero_puertas
        self.tipo = "Coche"

    def acelerar(self):
        print("El coche está acelerando")    
from abc import ABC, abstractmethod

class Figura3D(ABC):

    def __init__(self):
        pass
    # Creamos los metodos que deberan ser usados por todas las clases
    @abstractmethod
    def calcular_volumen(self):
        pass
    @abstractmethod
    def calcular_area_superficial(self):
        pass
from Animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self._raza = raza

    def ladrar(self):
        print("¡Guauuuuu!")
        
    def hablar(self):
        print("¡¡¡Guauu... Guauu!!!")
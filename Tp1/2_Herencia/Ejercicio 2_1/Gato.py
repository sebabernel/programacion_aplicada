from Animal import Animal
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self._color = color

    def maullar(self):
        print("¡Miauuuuuuu!")

    def hablar(self):
        print("¡¡Miauuu... Miauuu!!")
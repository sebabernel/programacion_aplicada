from Libro import Libro

class Libreria(Libro):

    def __init__(self):
        self.lista_libros = []
    
    def agregar_libro(self, libro):
        self.lista_libros.append(libro)

    def calcular_precio_total(self):
        precio_total = 0
        for libro in self.lista_libros:
            precio_total += libro.precio
        return precio_total
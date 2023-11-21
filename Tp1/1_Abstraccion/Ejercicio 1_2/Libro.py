
class Libro: 

    def __init__(self, titulo, autor, precio):
        self._titulo = titulo
        self._autor = autor
        self._precio = precio

    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def precio(self):
        return self._precio
    
    
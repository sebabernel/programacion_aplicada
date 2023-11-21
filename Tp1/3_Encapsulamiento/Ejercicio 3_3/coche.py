class Coche:
    def __init__(self, velocidad: float, kilometraje: float):
        self._velocidad = velocidad
        self.kilometraje = kilometraje

    @property
    def velocidad(self):
        return self._velocidad
    
    def acelerar(self, incremento: float):
       
       if incremento > 0:
           self._velocidad += incremento
           print(f"Acelerando. Nueva velocidad: {self._velocidad} km/h")
       else:
           print("La aceleracion debe ser mayor a cero.")

    def registrar_kilometraje(self, distancia: float):
        if distancia >= 0:
            self.kilometraje += distancia
            print("Nuvo Kilometraje registrado.")
        else:
            print("La distancia debe ser mayor que cero.")

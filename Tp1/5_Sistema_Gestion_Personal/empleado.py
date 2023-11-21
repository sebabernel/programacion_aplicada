from persona import Persona

class Empleado(Persona):

    def __init__(self, nombre, edad, dni, salario, cargo):
        super().__init__(nombre, edad, dni)
        self._salario = salario
        self._cargo = cargo

    @property
    def salario(self):
        return self._salario
    @property
    def cargo(self):
        return self._cargo
    
    def calcular_salario(self):
        # este metodo calculael salario segun el cargo
        if self._cargo == "junior":
            return self._salario * 1.2 # incrementa el basico un 20%
        elif self._cargo == "Senior":
            return self._salario * 1.5 # incrementa el basico un 50%
        else:
            return self._salario
        
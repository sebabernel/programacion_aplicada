from empleado import Empleado

class Gerente(Empleado):
    
    def __init__(self, nombre, edad, dni, salario, cargo, departamento):
        super().__init__(nombre, edad, dni, salario, cargo)
        self._departamento = departamento

    @property
    def departamento(self):
        return self._departamento
    
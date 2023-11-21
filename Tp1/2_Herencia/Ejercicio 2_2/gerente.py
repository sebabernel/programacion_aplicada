from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, area):
        super().__init__(nombre, salario, departamento)
        self._area = area

def contratar(self):
    print("Contratando nuevo empleado")

def despedir(self):
    print("Despidiendo empleado...")
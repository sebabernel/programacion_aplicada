from empleado import Empleado

class Trabajador(Empleado):
    def __init__(self, nombre, salario, departamento, turno):
        super().__init__(nombre, salario, departamento)
        self._turno = turno


    def trabajar(self):
        print("Trabajador operetivo para tomar tareas")

    def descansar(self):
        print("Empleado en turno de descanso")


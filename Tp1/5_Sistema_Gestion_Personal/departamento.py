from empleado import Empleado
class Departamento:
    
    def __init__(self):
        self._empleados = []

    def agregar_empleado(self, empleado):
        self._empleados.append(empleado)

    def eliminar_empleado(self, empleado):
        self._empleados.remove(empleado)

    def consultar_empleado(self):
        return self._empleados
    

from empleado import Empleado
from trabajador import Trabajador
from gerente import Gerente

empleado1 = Empleado("Romina", 200000, "Ventas")
empleado2 = Empleado("Fabiana", 400000, "Marketing")


gerente1 = Gerente("Messi", 9000000, "Operaciones", "Produccion")
gerente2 = Gerente("Maradona", 8000000, "Finanzas", "Contabilidad")

trabajador1 = Trabajador("Samuel", 500000, "Mantenimiento", "Nocturno")
trabajador2 = Trabajador("Sofia", 300000, "Recursos Humanos", "Diurno")

print("Empleados"+ "-------------"+" Salario")
print("-----------------------------")
print(empleado1._nombre,   "-------------", empleado1._salario)
print(empleado2._nombre,   "-------------", empleado2._salario)
print(gerente1._nombre,    "-------------", gerente1._salario)
print(gerente2._nombre,    "-------------", gerente2._salario)
print(trabajador1._nombre, "-------------", trabajador1._salario)
print(trabajador2._nombre, "-------------", trabajador2._salario)
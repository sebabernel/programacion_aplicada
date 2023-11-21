from persona import Persona
from empleado import Empleado
from departamento import Departamento
from gerente import Gerente


# Instanciamos las Clases
juanPerez = Persona("Juan Perez", 30, "23456932")
anaLopez = Empleado("Ana Lopez", 25, "24990320", 30000, "Junior")
carlosRodriguez = Gerente("Carlos Rodriguez", 58, "21345234", 500000, "Senior", "IT")
# Crear departamento
departamento_it = Departamento()

# Agregar empleados al departamento
departamento_it.agregar_empleado(anaLopez)
departamento_it.agregar_empleado(carlosRodriguez)

# Consultar empleados del Departamento
empleado_departamento = departamento_it.consultar_empleado()
for empleado in empleado_departamento:
    print(f"Empleado: {empleado.nombre} \nCargo: {empleado.cargo}")
print("-------------------------------------------")

# Calcular salario de un empleado
salario_calculado = anaLopez.calcular_salario()
print(f"El salario calculado para {anaLopez.nombre} es: {salario_calculado}")

print("-------------------------------------------")
# Accder a informacion
print(f"{carlosRodriguez.nombre} - Departamento: {carlosRodriguez.departamento}")
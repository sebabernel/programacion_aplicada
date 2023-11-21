

class Empleado:
    def __init__(self, nombre, salario, departamento):
        self._nombre = nombre
        self._salario = salario
        self._departamento = departamento

    def calcular_salario(self):
        # Calcula salario para empleado
        return self._salario


class Trabajador(Empleado):
    
    def __init__(self, nombre, salario, departamento, turno):
        super().__init__(nombre, salario, departamento)
        self._turno = turno


        """ Metodo para calcular el salario del trabajador"""
    def calcular_salario(self):
        
        salario = self._salario + 10000
        if self._turno == "Nocturno":
            salario += 5000
        return salario
    

class Gerente(Empleado):

    def __init__(self, nombre, salario, departamento, area):
            super().__init__(nombre,salario, departamento)
            self._area = area

    """Metodo contratar, una de las funciones de Gerentes"""
    def contatar(self):
            print("Contratando nuevo empleado...")

    
# Instanciamos empleados

empleado1 = Empleado("Romina", 250000, "Ventas")
empleado2 = Empleado("Fabiana", 40000, "Marketing")
gerente1 = Gerente("Messi", 900000, "Operaciones", "Produccion")
gerente2 = Gerente("Maradona", 900000, "Finanzas", "Contabilidad")
trabajador1 = Trabajador("Samuel", 540000, "Mantenimiento", "Nocturno")
trabajador2 = Trabajador("Erica", 250000, "RRHH", "Diurno")

# Creamor una lista de empleados de diferentes tipos
lista_empleados = [empleado1, empleado2, gerente1, gerente2, trabajador1, trabajador2]


# Con polimorfismo calculamos sus salarios 
for empleado in lista_empleados:
     print(f"Nombre: {empleado._nombre}  ------------  Salario: {empleado.calcular_salario()}")     


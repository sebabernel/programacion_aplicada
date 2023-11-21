"""Decoradores 
 # 1.1.   Hacer un decorador para registrar las llamadas a una función, junto con  sus argumentos y resultados.
 # 1.2.   Hacer un decorador para verificar que los argumentos de una función  sean del tipo correcto. 
 # 1.3.   Hacer un decorador para agregar un retardo antes de que se ejecute  una función
 # 1.4.   Hacer un decorador para verificar las precondiciones antes de ejecutar  una función """


# Se define un decorador para registrar las llamadas a una funcion
def registrar(func):
    # lista para almacenar los registros
    registros = []
    # funcion envoltura que recibe los mismos argumentos que la funcion original
    def wrapper(*args, **kwargs):
        # Llama a la funcion original y guarda el resultado 
        resultado = func(*args, **kwargs)
        # Crear un registro con el nombre de la funcion, los argumentos y el resultado
        registro = f" {func.__name__}({', '.join(map(repr, args))}{', ' if args and kwargs else ''}{', '.join(f'{k}= {v!r}' for k, v in kwargs.items())}) -> {resultado!r}"
        # Para añadir el registro a la lista de registros
        registros.append(registro)
        # Devuelve el resultado
        return resultado
    # Añadir un archivo a la funcion wrapper para acceder a la lista de registros
    wrapper.registros = registros
    # Devolver la funcion que envuelve
    return wrapper

# usar el decorador para registrar las llamadas a una funcion de ejemplo
@registrar
def suma(a, b):
    return a + b
@registrar
def resta(a, b):
    return a - b
@registrar
def multiplicar(a, b):
    return a * b


# Se llama a funciones con diferentes argumentos
suma(4, 6)
suma(5, 5)
suma(a = 23, b = 32)
resta(3, 6)
multiplicar(5, 5)


# Muestra los registros de las llamadas 
for registro in suma.registros:
    print(registro)
for registro in resta.registros:
    print(registro)
for registro in multiplicar.registros:
    print(registro)





"""
# Machete para decorador
def nombre_decorador(funcion):
    def wrapper(*args, **kwargs):
        # Se hace algo antes
        resultado = funcion(*args, **kwargs)
        # Se hace algo despues

        return resultado # se retorna el resultado
    
    #devuelve la funcion
    return wrapper"""
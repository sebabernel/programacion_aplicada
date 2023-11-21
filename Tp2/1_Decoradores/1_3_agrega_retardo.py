import time
def retardo(segundos):
    def decorador(func):
        def wrapper(*args, **kwargs):
            # Imprime un mensaje antes de que la funcion original sea ejecutada
             print(f"Espero {segundos} segundos antes de ejecutar {func.__name__}...")
             # Agregamos el retardo usando la funcion otra funcion
             time.sleep(segundos)
             # Llamo a fucnion original con los argumentos originales
             resultado = func(*args, **kwargs)
             # Delvemos el resulado de la funcion original
             return resultado
        # Devuelvo la funcion en voltorio
        return wrapper
    return decorador

# Aplicamos el decorador con un retardo de 3 segundos a una funcion especifica
@retardo(4)
def funcion_a_decorar():
    print("¡La funcion original ha sido ejecutada")

# Llamo a la funcion decorada
funcion_a_decorar()

"""Programación concurrente / paralelo """

"""9.1. Crea dos hilos que ejecuten dos funciones diferentes simultáneamente  y muestran mensajes de salida.""" 
import threading
import time
print("Ejercicio: 9.1")
def func_1():
    for _ in range(5):
        print("funcion 1")
        time.sleep(2) # Simula entrada y salida

def func_2():
    for _ in range(5):
        print("2 Funcion activada")
        time.sleep(2) # simula entrada y salida

# Creamos los hilos, cada uno para una funcion
hilo_1 = threading.Thread(target=func_1)
hilo_2 = threading.Thread(target=func_2)

# iniciamos los hilos 
hilo_1.start()
hilo_2.start()

# Espero a que ambos hilos terminen
hilo_1.join()
hilo_2.join()

print("Ambos hilos han terminado. ")

"""9.2. Implementa el problema del productor-consumidor utilizando hilos,  donde un hilo produce datos y otro hilo los consume 
     desde una cola  compartida."""
print("Ejercicio: 9.2")
import queue
"""
# Creo una cola compartida con n tamaño mixto
cola_compartida = queue.Queue(maxsize = 5)
# Creo funcion para hilo productor
def productor():
    for i in range(10):
        dato = f'Dato---{i}'
        cola_compartida.put(dato)
        print(f'Productor produjo: {dato}')

def consumidor():
    while True:
        dato = cola_compartida.get()
        print(f'Consumidor consumio: {dato}')
        time.sleep(2)
        cola_compartida.task_done()

# Creo los hilos para el productor y el consumidor
hilo_productor = threading.Thread(target = productor)
hilo_consumidor = threading.Thread(target = consumidor)

# Inicializo los hilos con el metodo start
hilo_productor.start()
hilo_consumidor.start()


# Esperar a que terminen
hilo_productor.join()
hilo_consumidor.join()
"""
""" 9.3. Crea dos procesos utilizando la biblioteca multiprocessing y ejecuta  funciones diferentes en cada proceso.""" 
print("Ejercicio: 9.3")
import multiprocessing

# Creamos nueva cola para practicar
cola_nueva = multiprocessing.Queue(maxsize = 5)
# Funcion para el primer proceso
def proceso_uno():
    print("Soy la funcion ejecutandome")

def proceso_dos():
    print("Ahora me ejecuto, yo")

if __name__ == "__main__":

    # Creamos los procesos

    proceso_1 = multiprocessing.Process(target = proceso_uno)
    proceso_2 = multiprocessing.Process(target = proceso_dos)

    # Inicio los procesos
    proceso_1.start()
    proceso_2.start()

    # Esperar a que los procesos terminen
    proceso_1.join()
    proceso_2.join()




"""9.4. Utiliza un pool de procesos para realizar operaciones en paralelo en  una lista de datos."""

print("Ejercicio: 9.4")

# Función que realiza la operación con cada elemento de la lista
def operacion_en_paralelo(elemento):
    resultado = elemento * 2 
    return resultado

if __name__ == "__main__":
    # Lista de datos
    datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Número de procesos en el pool (según hardware)
    num_procesos = multiprocessing.cpu_count()

    # Crear un pool de procesos
    with multiprocessing.Pool(processes=num_procesos) as pool:
        # Aplicar la operación en paralelo a cada elemento de la lista
        resultados = pool.map(operacion_en_paralelo, datos)

    # Imprimir los resultados
    print("Lista original:", datos)
    print("Lista después de la operación en paralelo:", resultados)  


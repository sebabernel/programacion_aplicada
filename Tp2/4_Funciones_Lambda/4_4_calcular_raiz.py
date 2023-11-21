"""4.4.   Toma una lista de números y utiliza map con una función lambda para  calcular la raíz cuadrada de cada número"""
from math import sqrt
# importacion absoluta del modulo math el metodo sqrt

# Creo lista de numeros
numeros = [4, 9, 16, 25, 36, 49, 64, 81]

# Con Map y funcion Lambda calculo la raiz cuadrada de cada numero

raiz_cuadrada = list(map(lambda x: int(sqrt(x)), numeros)) # para que el resultado sea entero se envuelve el metodo en int


# Imprimir resultado
print(raiz_cuadrada)

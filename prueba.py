# Archivo para correr todas funciones y conceptos aprendidos
import time
print("************** Decoradores **************")
def predicion(*condiciones):
    def verificar(funcion):
        def wrapper(*args, **kwargs):
            for condicion in condiciones:
                if not condicion(*args, **kwargs):
                    print("No se cumple con al condicion")
                    return
                resultado = funcion(*args, **kwargs)
            return resultado
        return wrapper
    return verificar

@predicion(lambda x: x > 0)
def predice(x):
    print("Si sale esta escritura es porque funcionaste corrctamente")

predice(3)
predice(-2)

def registrar(funcion):
    registros = []
    def wrapper(*args, **kwargs):
        resultado = funcion(*args, **kwargs)
        registro = f"{funcion.__name__}({', '.join(map(repr, args))}{', ' if args and kwargs else ''}{', '.join(f'{k}={v!r}' for k, v in kwargs.items())})-> {resultado!r}"
        registros.append(registro)
        return resultado
    wrapper.registros = registros
    return wrapper

@registrar
def suma(a, b):
    return a + b
suma(5, 7)

for registro in suma.registros:
    print(registro)

def verificador(funcion):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError(f"{arg} no es valido para la funcion")
        resultado = funcion(*args, **kwargs)
        return resultado
    return wrapper

@verificador
def sumar(a, b):
    return a + b

print("la suma de ", sumar(5, 6)) 
print("*********   Decorador Verificador de tipo de datos *********")

def verificar(*tipos):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            for i, arg in enumerate(args):
                if not isinstance(arg, tipos[i]):
                    raise TypeError(f"El tipo {i + 1} no corresponde al tipo de dato {tipos[i]}")
            return funcion(*args, **kwargs)
        return wrapper
    return decorador

@verificar(int, int, str)
def comprobar(a, b, texto):
    print("si esta bien escrita el decorador saldra este texto")

comprobar(2, 3, "salta")

def verificamos(*tipos):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            for i, arg in enumerate(args):
                if not isinstance(arg, tipos[i]):
                    raise TypeError(f"El tipo de datos {i+1} no corresponde al tipo {tipos[i]}")
            return funcion(*args, **kwargs)
        return wrapper
    return decorador

@verificamos(int, int)    
def probar(numero, num):
    print(f"ingresaste correctamente {numero}{num}")

probar(3, 5)
print("***********  Decorador Retardo ****************")
def retardo(segundos):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            time.sleep(segundos)
            return funcion(*args, **kwargs)
        return wrapper
    return decorador


@retardo(1)
def probando():
    print("--    --")

print("************** Administrador de Contenidos **********")
class Juego:
    def __init__(self, mensaje):
        self.mensaje = mensaje
    
    def __enter__(self):
        print(f" - Ingresando {self.mensaje}")
        return self

    def __exit__(self, tipo, valor, trazado):
        print(f" - Saliendo  {self.mensaje}")


with Juego("juego ajedrez")as ac:
    print("Bienvenido al juego")
    probando()

import os

class AdminDirectorio:
    def __init__(self, ruta):
        self.ruta = ruta

    def __enter__(self):
        self.original = os.getcwd()
        os.chdir(self.ruta)
        numeros = [1, 2, 3, 4, 5]
        resultado = list(map(lambda x: x * 2, numeros))
        for res in resultado:
            print(f"el numero es {res}")
            probando()
        cadenas = ["cadena", "para", "aprobar", "materia", "Primer"]
        cambiar = list(map(lambda x: x.upper(), cadenas))
        contar_cadena = list(map(lambda x: len(x), cadenas))
        for cam in cambiar:
            print(cam)
            print(f"En minusculas {cam.lower()}")
            print(f"Tiene {len(cam)} caracteres")
            probando()
        
        return self
    def __exit__(self, tipo, valor, trazado):
        os.chdir(self.original)
from math import sqrt
with AdminDirectorio(r"C:\Users\vonpaton") as ad:
    print(f"Ingresa en directorio {os.getcwd()}")
    probando()
print(f"ahora esta en este directorio ++++++++ {os.getcwd()}")
probando()
print("********* Funciones Lambda (x: x, lista)**********")
num = [4, 9, 16, 25, 36, 49, 64, 81, 100]
resultado = list(map(lambda x: x ** 2, num))
raiz = list(map(lambda x: int(sqrt(x)), num))
for resul in resultado:
    print(f"El cuadrado es {resul}")
for resul in raiz:
    print(resul)
    probando()
cadenas= ["soy", "la", "Mejor", "cadena", "que", "existe"]
raaices = list(map(lambda x: int(sqrt(x)), num))
multiplicacion = map(lambda x: x * 2, num)
cuadrado = list(map(lambda x: x ** 2, num))
mayusculas = list(map(lambda x: x.upper(), cadenas))
minusculas = list(map(lambda x: x.lower(), cadenas))
contar_cadena = list(map(lambda x: len(x), cadenas))
# Probando funcion zip, se detiene en la cadena mas corta
print("Probano recorrer funcion zip con un for, para recorrer varias listas a la vez")
for raiz, cadena, producto, may, min, cont in zip(raaices, cadenas, multiplicacion, mayusculas, minusculas, contar_cadena):
    print(raiz, cadena, producto, may, min, cont)
print("***********  5.1 Algoritmos ***********")
def suma_digitos(numero):
    if numero < 0:
        return numero + 1
    elif numero % 2 == 0:
        sumaDigito = sum(int(digito) for digito in str(numero))
        return sumaDigito
    else:
        numero -= 3
        sumaDigito = sum(int(digito) for digito in str(numero))
        return sumaDigito
    
num = 121
print(suma_digitos(num))
probando()
print("************   Recursividad  *************")

def salir(numero):

    if numero == 0:
        print("Por fin puedo salir")
        return
    else:
        print(numero)
        probando()
        salir(numero - 1)

salir(5)

def suma_primo(numero, contar = 1, sumar = 0):
    if numero == 0:
        return sumar
    elif numero % contar == 0 and contar <= 2:
        return suma_primo(numero - 1, contar + 1, sumar + numero)
    else:
        return suma_primo(numero - 1, contar + 1, sumar)

print(suma_primo(14))

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)
    
a = 3
b = 5
mcd = mcd(a,b)
print(mcd)

def micd(a, b):

    if b == 0: 
        return a
    else:
        return micd(b, a % b)
    
def minimoMult(a, b):
    if b == 0:
        return a
    else:
        return minimoMult(b, a % b)
    
print(minimoMult(5, 10))


# Practica

def cad(cadena):
    if len(cadena) <= 1:
        return cadena
    else:
        return cadena[-1] + cad(cadena[: -1])

testop = "ragul nugal a yov aloh "
darvuelta = cad(testop)

print(darvuelta)
"""**************   Excepciones **************"""
print("********************* Excepciones  ************")

class DivisionPorCero(Exception):
    pass 
    def acceder_a_valor():

        try:
            numerador = float(input("Ingrese un numero: "))
            denominador = float(input("Ingrese segundo numero"))

            resultado = numerador / denominador
            print(f"El resultado de la division es {resultado}")
        
        except ZeroDivisionError:
            print("No se puede dividir por cero")
        except ValueError:
            print("Ingrese numeros validos")
            DivisionPorCero.acceder_a_valor()


class indiceFueraDeRango(Exception):
    def __init__(self, mensaje = "Indice de rango. "):
        self.mensaje = mensaje
        super().__init__(mensaje)

    def acceder_a_indice():
        numeros = [10, 20, 30, 40, 50]
        try: 
            indice = int(input("Ingrese un indice para acceder a la lista: "))

            elemento = numeros[indice]

            print(f"Elemento en el indice {indice}: {elemento}")

        except IndexError:
            print("Error: El indice está fuera de rango")

        except ValueError:
            print("Error: Ingrese un indice valido.")

class EntradaNoNumericaError(Exception):
    def __init__(self, mensaje = "Ingrese numeros validos."):
        self.mensaje = mensaje
        super().__init__(mensaje)

    def convertir_a_numero():
        try:
            cadena_numero = input("Ingrese una cadena que represente un número: ")
            numero = float(cadena_numero)

            print(f"Numero ingresado: {numero}")
        except ValueError:
            print("Error: La cadena no es un numero valido.")

class ArchivoNoEncontradoError(Exception):
    def __init__(self, mensaje = "El archivo no existe."):
        self.mensaje = mensaje
        super().__init__(mensaje)

    def abrir_archivo():
        try:
            archivo = open("archivo.txt", "r")
            contenido = archivo.read()
            archivo.close()
            print(contenido)
        except FileNotFoundError:
            print("Error: El archivo no existe.")

class ClaveNoExisteError(Exception):
    def __init__(self, mensaje = "La clave no existe"):
        self.mensaje = mensaje
        super().__init__(mensaje)

    def acceder_a_valor():
        diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Buenos Aires"}
        clave = input("Ingrese una clave: ")

        try:
            valor = diccionario[clave]
            print(f"El valor de {clave} es {valor}")
        except KeyError:
            print("Error: La clave no existe.")
            ClaveNoExisteError.acceder_a_valor()
        
    
ClaveNoExisteError.acceder_a_valor()
EntradaNoNumericaError.convertir_a_numero()
indiceFueraDeRango.acceder_a_indice()
DivisionPorCero.acceder_a_valor()
ArchivoNoEncontradoError.abrir_archivo()

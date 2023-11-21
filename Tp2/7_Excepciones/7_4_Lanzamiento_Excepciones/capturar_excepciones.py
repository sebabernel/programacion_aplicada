"""Lanzamiento de excepciones 
 7.4.1.   Capturar las siguientes excepciones personalizadas en el punto 7.2, imprimir  un mensaje en pantalla y lanzarlas nuevamente"""# 7.1.1


print("7.4.1.")
class DivisionPorCeroError(Exception):
    def __init__(self, mensaje="No se puede dividir por cero."):
        super().__init__(mensaje)

def realizar_division():
    try:
        numerador = float(input("Ingrese un numero: "))
        denominador = float(input("Ingrese denominador: "))

        if denominador == 0:
            raise DivisionPorCeroError()

        resultado = numerador / denominador
        print(f"El resultado de la división es: {resultado}")

    except DivisionPorCeroError as e:
        print(f"Error: {e}")

    except ValueError:
        print("Error: Ingrese números válidos.")

class IndiceFueraDeRangoError(Exception):
    def __init__(self, mensaje="Índice fuera de rango."):
        super().__init__(mensaje)

def acceder_a_indice():
    numeros = [10, 20, 30, 40, 50]

    try:
        indice = int(input("Ingrese un índice para acceder a la lista: "))
        if indice < 0 or indice >= len(numeros):
            raise IndiceFueraDeRangoError()

        elemento = numeros[indice]
        print(f"Elemento en el índice {indice}: {elemento}")

    except IndiceFueraDeRangoError as e:
        print(f"Error: {e}")

    except ValueError:
        print("Error: Ingrese un índice válido.")

class EntradaNoNumericaError(Exception):
    def __init__(self, mensaje="Ingrese números válidos."):
        super().__init__(mensaje)

def convertir_a_numero():
    try:
        cadena_numero = input("Ingrese una cadena que represente un número: ")
        numero = float(cadena_numero)
        print(f"Número ingresado: {numero}")

    except EntradaNoNumericaError as e:
        print(f"Error: {e}")

    except ValueError:
        print("Error: La cadena no es un número válido.")

class ArchivoNoEncontradoError(Exception):
    def __init__(self, mensaje="El archivo no existe."):
        super().__init__(mensaje)

def abrir_archivo():
    try:
        archivo = open("archivo.txt", "r")
        contenido = archivo.read()
        archivo.close()
        print(contenido)

    except ArchivoNoEncontradoError as e:
        print(f"Error: {e}")

    except FileNotFoundError:
        print("Error: El archivo no existe.")

class ClaveNoExisteError(Exception):
    def __init__(self, mensaje="La clave no existe."):
        super().__init__(mensaje)

def acceder_a_valor():
    diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Buenos Aires"}
    clave = input("Ingrese una clave: ")

    try:
        valor = diccionario[clave]
        print(f"El valor de {clave} es {valor}")

    except ClaveNoExisteError as e:
        print(f"Error: {e}")

    except KeyError:
        print("Error: La clave no existe.")

# Llamada a las funciones
realizar_division()
acceder_a_indice()
convertir_a_numero()
abrir_archivo()
acceder_a_valor()
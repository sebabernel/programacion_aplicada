"""Para cada caso anterior del manejo de excepciones (7.1.1, 7.1.2,  7.1.3, 7.1.4, 7.1.5)
 crear una excepción personalizada"""

# 7.1.1
class DivisionPorCero(Exception):
    def __init__(self, mensaje = "No se puede divir por cero"):
        self.mensaje = mensaje
        super().__init__(self, mensaje)

    def realizar_division():
        try:
            # Solicitar numeros a usuario
            numerador = float(input("Ingersel un numero: "))
            denominador = float(input("Ingrese denominador: "))

            # Raliza la division
            resultado = numerador / denominador
            #~Imprime resultado

            print(f"El Resulatado de la division es: {resultado}")

        except ZeroDivisionError:
            # Maneja el excepcion si el denominador es cero.
            print("Error: No se puede dividir por cero.")
        except ValueError:
            # Maneja la excepcion si no ingresa un numero
            print("Ingrese numeros validos")

# 7.1.2
class IndiceFuersaDeRangoError(Exception):
    def __init__(self, mensaje = "Indiceguera de rango."):
        self.mensae = mensaje
        super().__init__(self, mensaje)

    def acceder_a_indice():
        # Crear una lista de números
        numeros = [10, 20, 30, 40, 50]

        try:
            # Solicita un indice
            indice = int(input("Ingrese un índice para acceder a la lista: "))

            # accede al elemento en el índice proporcionado
            elemento = numeros[indice]

            # Imprimir el elemento
            print(f"Elemento en el índice {indice}: {elemento}")

        except IndexError:
            # Maneja la excepción si el índice está fuera de rango
            print("Error: El índice está fuera de rango.")
            # Con recursividad vuelve a pedir el indice

        except ValueError:
            # Maneja la excepción si el usuario ingresa algo que no es un número
            print("Error: Ingrese un índice válido.")
            # Maneja la excepción si el usuario ingresa algo que no es un número



# 7.1.3
class EntradaNoNumericaError(Exception):
    def __init__(self, mensaje = "Ingrese numeros validos."):
        self.mensaje = mensaje
        super().__init__(self, mensaje)
            
    def convertir_a_numero():
        try:
            # Pedir al  usuario que ingrese una cadena que represente un número
            cadena_numero = input("Ingrese una cadena que represente un número: ")
            numero = float(cadena_numero)

            # Imprimir el número
            print(f"Número ingresado: {numero}")

        except ValueError:
            # Maneja la excepción si la cadena no se puede convertir a un número
            print("Error: La cadena no es un número válido.")
            # Aplicamos recursividad


# 7.1.4
class ArchivoNoEncontradoError(Exception):
    def __init__(self, mensaje = "El archivo no existe."):
        self.mensaje = mensaje
        super().__init__(self, mensaje)
            
    def abrir_archivo():
        try:
            # codigo para abrir un archivo
            archivo = open("archivo.txt", "r")
            contenido = archivo.read()
            archivo.close()
            print(contenido)
            # Maneja la excepción si el archivo no se encuentra
        except FileNotFoundError:
            print("Error: El archivo no existe.")


# 7.1.5
class ClaveNoExisteError(Exception):
    def __init__(self, mensaje = "La clave no existe"):
        self.mensaje = mensaje
        super().__init__(self, mensaje)

            
    def acceder_a_valor():
        # Creo diccionario
        diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Buenos Aires"}
        clave = input("Ingrese una clave: ")

        try:
            # accedo a un valor con una clave
            valor = diccionario[clave]
            # Imprime clave valor
            print(f"El valor de {clave} es {valor}")
        except KeyError:
            # Maneja la excepción si la clave no existe en el diccionario
            print("Error: La clave no existe.")
            # Practicamos recursividad
    
""" Excepciones 

 7.1.1.  Escribe un programa que solicite al usuario dos números y realice  la división de uno por el otro.
   Utiliza un bloque try y except para  manejar la excepción que ocurre si el segundo número es cero.""" 
 
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
        # Usa recursividad para seguir en el algoritmo
        realizar_division()
    except ValueError:
        # Maneja la excepcion si no ingresa un numero
        print("Ingrese numeros validos")
        # Llama nuevamente a la funcion
        realizar_division()
# Llama a la funcion para realizar la division
realizar_division() 


"""7.1.2. Crea una lista de números y, a continuación, intenta acceder a un  elemento en un índice especificado por el usuario. Utiliza un 2 
 bloque try y except para manejar la excepción que se produce si  el índice está fuera de rango."""
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
        acceder_a_indice()

    except ValueError:
        # Maneja la excepción si el usuario ingresa algo que no es un número
        print("Error: Ingrese un índice válido.")
        # Maneja la excepción si el usuario ingresa algo que no es un número
        acceder_a_indice()

# Llamar a la función para acceder a un índice en la lista
acceder_a_indice()


"""7.1.3. Solicita al usuario que ingrese una cadena que represente un  número. Utiliza un bloque try y except para manejar la excepción
 que se produce si la cadena no se puede convertir a un número.  """
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
        convertir_a_numero()

convertir_a_numero()
 

"""7.1.4.   Escribe un programa que intente abrir un archivo que no existe y 
 utilice un bloque try y except para manejar la excepción de  "FileNotFoundError"."""

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

abrir_archivo()

"""7.1.5.   Crea un diccionario y luego intenta acceder a un valor utilizando  una clave que no está en el diccionario. Utiliza un bloque try y  
except para manejar la excepción que se produce si la clave no  existe."""

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
        acceder_a_valor()
 
# Llamar a la función para acceder a un valor con una clave no existente
acceder_a_valor()
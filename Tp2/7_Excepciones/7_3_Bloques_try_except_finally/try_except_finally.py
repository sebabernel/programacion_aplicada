"""Bloques try-except-finally 
 7.3.1.Escribe un programa que intente abrir un archivo, leer su  contenido y luego cerrarlo. Utiliza bloques try, except y finally 
  para asegurarte de que el archivo se cierre correctamente,  incluso si ocurre una excepción durante la lectura.  """

print("7.3.1")   
def leer_archivo(nombre_archivo):
    try:
        # Indica el archio para abrir en modo lectura
        archivo = open(nombre_archivo, "r")

        try:
            # Lee el contendio del archivo
            contenido = archivo.read()
            print(f"Contenido del archivo: \n{contenido}")

        except Exception as e:
            # Maneja cualquier excepcion que ocurra durante la lectura
            print(f"Error durante la lectura")

        finally:
            # Asegura de cerrar el archivo, incluso si huna una excepcion
            archivo.close()
            print("Archivo cerrado coerrectamente.")
    except FileNotFoundError:
        # Maneja la excepcion si el archivo no se encuentra
        print("Error: El archivo no existe.")


# nombre del archio a leer 
nombre_archivo = "sebas.txt"
leer_archivo(nombre_archivo)


"""7.3.2. Crea un programa que solicite al usuario dos números y una  operación matemática (suma, resta, multiplicación, división) 
para  realizar. Utiliza bloques try, except y finally para manejar cualquier  excepción que pueda ocurrir durante la operación y asegurarte  
de que los recursos se liberen correctamente. """

print("7.3.2")   

def realizar_operacion():
    try:
        # Solicitar dos numeros y operacion)
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operacion = input("Ingrese la operacion a realizar (+, -, *, /): ")

        # Realiza la operacion segun lo seleccionado
        if operacion == '+':
            resultado = num1 + num2
            print(f"Resultado de la suma es: {resultado}")
        elif operacion == '-':
            resultado = num1 - num2
            print(f"Resultado de la resta es: {resultado}")
        elif operacion == '*':
            resultado = num1 * num2
            print(f"Resultado de la multiplicacion es: {resultado}")
        elif operacion == '/':
            if num2 != 0:  # Verificar que el divisor no sea cero
                resultado = num1 / num2
                print(f"Resultado de la division es: {resultado}")
            else:
                raise ValueError("No se puede dividir por cero.")
        else:
            raise ValueError("Operacion no valida.")

    except (ValueError, ZeroDivisionError) as e:
        # Maneja excepciones especificas
        print(f"Error: {e}")

    finally:
        # El bloque Finally asegura que los recursos se liberen correctamente.
        print("Operacion completada.")

# Se llama la funcion para chequear el código
realizar_operacion()

print("7.3.3")   
"""  Escribe un programa que abra un archivo, lea su contenido y  escriba el mismo 
contenido en otro archivo. Utiliza bloques try, except y finally para manejar cualquier excepción que pueda  ocurrir durante la lectura 
o escritura, y asegúrate de que ambos  archivos se 
cierren correctamente"""

def copiar_contenido(origen, destino):
    try:
        # Abre el archivo de origen en modo lectura
        with open(origen, 'r') as archivo_origen:
            try:
                # Leer el contenido del archivo de origen
                contenido = archivo_origen.read()
                with open(destino, 'w') as archivo_destino:
                    # Escribe el msimo contenido en el archivo de destino
                    archivo_destino.write(contenido)
            except Exception as e:
                # Maneja exption durante la lectura y escritura
                print(f"Error durante la lecura o escritura: {e}")
    except FileNotFoundError:
        # Maneja excepcion si el archivo de origen no se encuentra
        print("Error. El archivo de origen no existe.")        

    finally:
        # Bloque que aseugra qeu los recursos se leberen correctamente
        print("Operaccion completada, se movio de un archivo a otro.")

# declaramos los archivos en variables, y llamamos a la funcion
origen = "otro.txt"
destino = "sebas.txt"
copiar_contenido(origen, destino)

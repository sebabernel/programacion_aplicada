"""Manejo de archivos 
 8.1. Escribe un programa que abra un archivo de entrada, lea su contenido y  luego escriba ese contenido
  en un nuevo archivo de salida. Asegúrate  de cerrar ambos archivos al final."""
print("8.1")

def copiar_contenido(archivo_entrada, archivo_salida):
  try:
    # Abrir el archivo para leer r
    with open(archivo_entrada, 'r') as entrada:
      # Leo el contenido del archivo de entrada
      contenido =entrada.read()

      #abrir el archivo de saldida en modo escritura
      with open(archivo_salida, 'w') as salida:
        salida.write(contenido)

        print("Contenido copiado con exito.")

  except FileNotFoundError:
    print(f"Error: El archivo {archivo_entrada} no existe.")
  except Exception as e:
    print(f"Error inespearado: {e}")

if __name__ == "__main__":
  # nombre del archvo de entrada
  archivo_entrada = "sebas.txt"
  archivo_salida = "otro.txt"
  #llamamos a la funcion para copiar contenido
  copiar_contenido(archivo_entrada, archivo_salida)

"""8.2.   Escribe un programa que abra un archivo de texto, cuente cuántas  palabras contiene y muestre el resultado en la pantalla."""

print("8.2")

def contar_palabras(nombre_archivo):
  try: 
    # Abrimos el archivoen modo lectura
    with open(nombre_archivo, 'r') as archivo:
      
      #leer el contenido del archivo
      contenido = archivo.read()

      # Dividir el contenido en palabras usando el espacio como delimitador
      palabras = contenido.split()
      # Contar la cantidad de palabras
      cantidad_palabras = len(palabras)

      # Mostrar el resultado en pantalla
      print(f"El archivo '{nombre_archivo}' contiene {cantidad_palabras}")

  except FileNotFoundError:
    print(f"Error: el archivo {nombre_archivo} no existe.")
  except Exception as e:
    print(f"Error inesperado: {e}")

if __name__ == "__main__":
  archivo_texto = "sebas.txt"
  
  contar_palabras(archivo_texto)

"""8.3.   Lee un archivo CSV que contiene registros de datos y realiza alguna  operación de procesamiento en los datos, cómo calcular 
  promedios,  encontrar valores máximos o mínimos, o filtrar registros que cumplan  ciertas condiciones."""
print("8.3")

import csv
def calcular_promedio(archivo_csv):
  try: 
    # Abre y lee el archivo
    with open(archivo_csv, 'r') as archivo:
      lector_csv = csv.DictReader(archivo)

      # variables para calculos 
      total_notas = 0
      cantidad_registros = 0

      # Recorrer cada fila en el archivo CSV
      for fila in lector_csv:
        # Convierto la nota de cadena a numero
        nota = float(fila['Nota'])

        # Suma la nota
        total_notas += nota
        cantidad_registros += 1

        #calcular promedio
        promedio = total_notas / cantidad_registros if cantidad_registros > 0 else 0
      
      # Muestra resultado
      print(f"El promedio de notas es: {promedio}")

  except FileNotFoundError:
    print(f"Error: El archivo {archivo_csv} no existe")
  except Exception as e:
    print(f"Error inesperado: {e}")

if __name__ == "__main__":
  archivo_csv = "sebas.csv"

  calcular_promedio(archivo_csv)



""" 8.4.Escribe un programa que tome varios archivos de texto y los concatena  en un solo archivo de salida. Asegúrate de cerrar todos 
  los archivos  correctamente. """
print("8.4")
# Litas de archivos
archivos = ["sebas.txt", "otro.txt"]
# nombre del archivo de salida
archivo_salida = "archivo_concatenado.txt"
try: 
  # Abro el archivo de salida en modo escriura
  with open(archivo_salida, 'w') as archivo_concatenado:
    # Concatenamos los archivos de texto
    for archivo in archivos:
      with open(archivo, 'r') as archivo_actual:
        contenido = archivo_actual.read()
        archivo_concatenado.write(contenido)
except FileNotFoundError:
  # Error si el archivo no existe
  print("Error: Uno o mas archivos no se encuntran.")

finally: 
  # Cerrar todos los archivos abiertos
  for archivo in archivos: 
    if 'archivo_actual' in locals():
      archivo_actual.close()
  if 'archivo_concatendado' in locals():
    archivo_concatenado.close()
print("Tarea completada")

"""8.5.   Lee un archivo CSV que contiene registros de datos y convertirlo en un  archivo JSON"""
print("8.5")
import json

archivo_json = 'datos.json'
archivo_csv = 'sebas.csv'

# Lista para almacenar los datos csv
datos = []
# Abrir el archivo csv en modo lectura
with open(archivo_csv, 'r') as csv_file:
  # Utilizar el lector de csv para procear el archivo
  csv_reader = csv.DictReader(csv_file)

  # Recorrer las filas del csv y agraglas a la lista
  for fila in csv_reader:
    datos.append(fila)

# Escribo la lista de diccionarios como un archivo json
with open(archivo_json, 'w') as json_file:
  json.dump(datos, json_file, indent=4)

print(f'Se ha convertido el archivo CSV "{archivo_csv}" a json. Archvio de salida: "{archivo_json}"')
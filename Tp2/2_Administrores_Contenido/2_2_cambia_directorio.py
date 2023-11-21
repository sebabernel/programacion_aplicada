"""Crea un administrador de contexto que permita cambiar el directorio de
  trabajo al entrar en un bloque y volver al directorio original al salir.  Ejemplo:"""
import os
class AdministradorDirectorio:
    def __init__(self, ruta):
        self.ruta = ruta
    
    def __enter__(self):
        # Comando que guarda el directorio original
        self.directorio_original = os.getcwd() # Metodo para obtener directorio de trabajo actual
        # Cambia al nuevo directorio
        os.chdir(self.ruta) # Metodo que cambia el directorio a la ruta proporcionada como parametro
        # Devuelve el objeto del administrador de contexto
        return self

    def __exit__(self, tipo_de_excepcion, valor_de_excepcion, traza_de_execpcion):
        # Metodo para restaurar el directorio original, de donde se guardo anteriormente
        os.chdir(self.directorio_original)

# Ejemplo de uso del administrador de contexto para cambiar a otra carpeta
with AdministradorDirectorio(r"C:\Users\vonpaton\Documents\Facultad 2023\Python_Facultad") as ad:
    print(f"Directorio actual: {os.getcwd()}")
    # representa a cualquier codigo que se quiera representar en el nuevo directorio

# Despues de salir del bloque 'with', el directorio de trabajo se restable al original
print(f"Directorio actual después de ejecutarse 'with: {os.getcwd()}")


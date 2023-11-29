"""Escribe una función recursiva para invertir una cadena"""


def invertir_cadena(cadena):
    # Colocamos la condicion sobre el tamaño de la cadena
    if len(cadena) <= 1:
        return cadena
    else:
        # Llamada recursiva de la funcion
        return cadena[-1] + invertir_cadena(cadena[: -1])


# Ejemplo

cadena_original = "Aprobaremos materia y celebraremos!!"

cadena_inivertir = invertir_cadena(cadena_original)

print(f"Cadena Original: {cadena_original}")
print("--------------------------------------")
print(f"Cadena Invertida: {cadena_inivertir}")

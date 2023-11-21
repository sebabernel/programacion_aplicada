"""4.3.   Dada una lista de cadenas, utiliza map y una función lambda para crear  una lista con la longitud de cada palabra."""

# Creo la cadena
cadena = ["palabras", "para", "contar", "en cadena"]

# Con Map y una funcion Lambda contamos las cadenas
contar_cadena = list(map(lambda x: len(x), cadena))


# Imprime resultado
print(contar_cadena)

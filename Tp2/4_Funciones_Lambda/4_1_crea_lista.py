"""4.1.   Dada una lista de números, utiliza map y una función lambda para crear  una nueva lista que contenga el doble de cada número."""

# Creamos lista de Numeros
numeros = [1, 2, 3, 4, 5]

# Con map y una funcion lambda devolvemos el doble de cada numero
resultado = list(map(lambda x: x * 2, numeros))

# Imprimimos la nueva lista
print(resultado)

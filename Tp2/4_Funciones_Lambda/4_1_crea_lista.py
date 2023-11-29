"""4.1.   Dada una lista de números, utiliza map y una función lambda para crear  una nueva lista que contenga el doble de cada número."""

# Creamos lista de Numeros
numeros = [1, 2, 3, 4, 5]

# Con map y una funcion lambda devolvemos el doble de cada numero
resultado = list(map(lambda x: x * 2, numeros))

# Imprimimos la nueva lista
print(resultado)

num = [3, 6, 9, 10, 13, 15]

resul = list(map(lambda x: x ** 2, num))

print(resul)


listar_num = [5, 10, 15, 20, 25]

sum_num = list(map(lambda x: x ** 3, listar_num))

print(sum_num)

""" Escribe una función recursiva para calcular el MCD de dos números  enteros"""

# Para calcular el mcd(minimo comun divisor)

def mcd(a, b):
    if b == 0:
        return a
    else: 
        # Llama la funcion nuevamente
        return mcd(b, a % b)


a = 5
b = 8

print(f"El mcd de {a} y {b} es {mcd(a, b)}")
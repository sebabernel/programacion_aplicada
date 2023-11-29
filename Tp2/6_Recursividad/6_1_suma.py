"""Escribe una función recursiva para encontrar y sumar todos los números  primos desde 1 hasta un número deseado"""

def suma_recursiva(numero, contar = 1, sumar = 0):
    if numero == 0: 
        
        return sumar
    elif numero % contar == 0 and contar <= 2:
        
        return suma_recursiva(numero - 1, contar + 1, sumar + numero)
    else:
        return suma_recursiva(numero - 1, contar + 1, sumar)        

    

print(suma_recursiva(15))    
        
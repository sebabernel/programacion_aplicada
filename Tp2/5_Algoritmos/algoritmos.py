"""Escribe una función que sume los dígitos de un número pares de un  número entero. Si el número es  impar, restarle 3 y  sumarlo. Si el número  da negativo, sumar 1"""

def suma_digitos_operacion(numero):
        # Condicion para verificar si el numero es par o impar
        
    if numero % 2 == 0:
            # En caso de que sea para suma los digitos
        suma_digitos = sum(int(digito) for digito in str(numero))
    else:
            # Si es impar, restar 3 y sumar los digitos
        resultado_temporal = numero - 3
            # Si el resultado es negativo, suma 1

        suma_digitos = sum(int(digito) for digito in str(resultado_temporal)) + 1

    return suma_digitos
    
# aplicamos

numero_par = 2468
resultado_par = suma_digitos_operacion(numero_par)
print(f"Resultado para numero par {resultado_par}")

numero_impar = 1357
resultado_impar = suma_digitos_operacion(numero_impar)
print(f"Resultado para numero par {resultado_impar}")
        

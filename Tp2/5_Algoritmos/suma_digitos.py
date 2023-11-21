

def sum_digits(num):
    # Verifica si el numero es negativo
    if num < 0:
        return num + 1
    # Verifica si el numero es par
    elif num % 2 == 0:
        # si es par, suma los digitos
        return sum(int(digit) for digit in str(num))
    else:
        # si es impar, resta 3
        return sum(int(digit) for digit in str(num - 3))
    

num = 12
print(sum_digits(num))

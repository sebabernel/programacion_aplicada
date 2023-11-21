def verificador_validador(func):
    # Verifica que todos los argumentos sena enteros
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Los argumentos deben ser entteros.")
        return func(*args, **kwargs)
    


@verificador_validador
def sumar(x, y):
    return x + y

# Se prueba verificador
print(sumar(5, 6))
print(sumar(5, 9))


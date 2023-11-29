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

def verificador_tipo(*tipos):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            for i, arg in enumerate(args):
                if not isinstance(arg, tipos[i]):
                    raise TypeError(f"El argumento {i+1} debe ser de tipo {tipos[i]}")
            return funcion(*args, **kwargs)
        return wrapper
    return decorador
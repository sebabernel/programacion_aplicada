# declaramos el decorador para cualquier ingreso
def precondiciones_decorator(*condiciones):
    # declaramos la funcion decoradora que toma argumento la funcion original o la que queremos decorar
    def decorator(func):
        # Definimos el envoltorio
        def wrapper(*args, **kwargs):
            # Verificamos cada condicion antes de ajecutar la funcion a evaluar
            for condicion in condiciones:
                if not condicion(*args, **kwargs):
                    # Si alguna condicion no se cumple, envia el siguiente mensaje
                    print(f"Error: No se cumplen las precondiciones para ejecutar {func.__name__}")
                    return
                # Si se cumplen las condiciones ejecuta la funcion original
                resultado = func(*args, **kwargs)
                # Retornamos el resultado de la funcion
                return resultado
            # Devolvemos la funcion que lo envuelve
            return wrapper
        # Delvolvemos el decorardor
        return decorator
    
# Funcon de ejemplo que tiene precondiciones, que x sea mayor a 0
@precondiciones_decorator(lambda x: x > 0)
def funcion_con_precondiciones(x):
    print(f"La funcion original ha sido ejecutada con x={x}")

# Llamar a la funcion decorada con precondiciones
funcion_con_precondiciones(3)  
# otra con condicion fuera de rango
#funcion_con_precondiciones(-4)


class Estudiante:
    def __init__(self, nombre, edad, calificaciones):
        self.__nombre = nombre 
        self.__edad = edad 
        self.__calificaciones = calificaciones
    # Metodos para accesos a atributos
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def calificaciones(self):
        return self.__calificaciones
    
    # Metodo publicos para establecer nuevas calificaciones
    def establecer_calificaciones(self, nueva_calificaciones):
        if self.validar_calificaciones(nueva_calificaciones):
            self.__calificaciones = nueva_calificaciones
            print("Calificacion ingresada con exito.")
        else:
            print("Las calificaciones deben ser numeros entre 0 y 10")
        return False
    
    
    def validar_calificaciones(self, calificaciones):
        if isinstance(calificaciones, list):
            return all(0 <= calificacion <= 10 for calificacion in calificaciones)
        return False


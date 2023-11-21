class Persona:
    def __init__(self, nombre, edad, dni):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre
    @property
    def edad(self):
        return self._edad
    @property
    def dni(self):
        return self._dni
    
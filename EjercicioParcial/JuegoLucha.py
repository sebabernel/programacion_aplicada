class Personaje:
    def __init__(self, nombre, raza, nivel, salud):
        self.nombre = nombre
        self.raza = raza
        self.nivel = nivel
        self.salud = salud

    def atacar(self, objetivo):
        danio = 10
        objetivo.recibir_danio(danio)

    def recibir_danio(self, danio):
        self.salud -= danio
    
class Movimiento:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def aplicar_efecto(self, personaje):
        pass

class Habilidad:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
    
    def activar(self, personaje):
        pass


class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.integrantes = []

    def agregar_personaje(self, personaje):
        pass

    def quitar_personaje(self, personaje):
        pass

class Elfo(Personaje):
    def __init__(self, nombre, nivel, salud):
        super().__init__(nombre, "Elfo", nivel, salud)
        
aragorn = Personaje("Aragorn", "Humano", 10, 100)
print(aragorn.nombre)
print(aragorn.salud)

aragorn.salud -= 20

corte_cruzado = Movimiento("Corte Cruzado", "Ofensivo")
corte_cruzado.aplicar_efecto(aragorn)

legolas = Elfo("Legolas", 8, 80)
legolas.atacar(aragorn)

print(legolas.nombre)
print(legolas.salud)
aragorn.atacar(legolas)

print(aragorn.nombre)
print(aragorn.salud)
print(legolas.nombre)
print(legolas.salud)


from Animal import Animal
from Perro import Perro
from Gato import Gato
from Pajaro import Pajaro

un_perro = Perro("Matute", 3, "Labrador")
print(un_perro._nombre)
un_perro.ladrar()
# Polimorfismo
un_perro.hablar()
print("--------------------------------")
un_gato = Gato("Mimosa", 5, "Naranja")
print(un_gato._nombre)
un_gato.maullar()
# Polimorfismo
un_gato.hablar()
print("--------------------------------")
un_pajaro = Pajaro("Loquillo", 4, "Carpintero")
print(un_pajaro._nombre)
un_pajaro.cantar()
# Polimorfismo
un_pajaro.hablar()
print("--------------------------------")


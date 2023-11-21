from figura_geometrica import Figura_Geometrica
from circulo import Circulo
from rectangulo import Rectangulo
from cuadrado import Cuadrado

figuras = [Circulo(5), Rectangulo(4, 5), Cuadrado(5)]

for figura in figuras:
    print(f"Informacion de la figura: ")
    print(f"Area: {figura._area}")
    print(f"Perimetro: {figura._perimetro}")
    print("-----------------------------------")
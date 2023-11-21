from Figura_Geometrica import Figura_Geometrica
from Circulo import Circulo
from Rectangulo import Rectangulo
from Triangulo import Triangulo
class App: 

    circulo = Circulo(5)
    rectangulo = Rectangulo(4, 6)
    triangulo = Triangulo(3, 4, 5, 2)

    print("------------------------------------------------")
    print("Circulo:")
    print(f"Area: {circulo.calcular_area()}")
    print(f"Perimetro: {circulo.calcular_perimetro()}")
    print("------------------------------------------------")

    print("Rectangulo:")
    print(f"Area: {rectangulo.calcular_area()}")
    print(f"Perimetro: {rectangulo.calcular_perimetro()}")
    print("------------------------------------------------")

    print("Triangulo:")
    print(f"Area: {triangulo.calcular_area()}")
    print(f"Perimetro: {triangulo.calcular_perimetro()}")
    print("------------------------------------------------")
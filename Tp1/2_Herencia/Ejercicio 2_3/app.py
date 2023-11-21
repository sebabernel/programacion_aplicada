from forma import Forma
from circulo import Circulo
from rectangulo import Rectangulo


# Instanciamos la  Forma
forma = Forma("Verde")
# Instanciamos el Circulo
circulo = Circulo("amarillo", 5)
print(f"Circulo Color: {circulo.color} \n Area: {circulo.calcular_area()} \n Perimetro: {circulo.calcular_perimetro()}")
# Instanciamos el Rectangulo
rectangulo = Rectangulo("verde", 10, 20)
print(f" Rectangulo Color: {circulo.color} \n Area: {rectangulo.calcular_area()} \n Perimetro: {rectangulo.calcular_perimetro()}")
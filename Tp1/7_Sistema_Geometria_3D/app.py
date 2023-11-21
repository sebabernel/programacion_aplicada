from punto3D import Punto3D
from cubo import Cubo
from esfera import Esfera
from cilindro import Cilindro

# Se intancian las Clases
punto1 = Punto3D(2, 3, 4)
cubo1 = Cubo(punto1, 4)
esfera1 = Esfera(punto1, 3)
cilindro1 = Cilindro(punto1, 3, 4)

# Calcular el volumen y area superficial de las figuras
print("Volumen del cubo:", cubo1.calcular_volumen())
print("Area superficial del cubo: ", cubo1.calcular_area_superficial())
print("---------------------------------")
print("Volumen de la esfera: ", esfera1.calcular_volumen())
print("Area superficial de la Esfera", esfera1.calcular_area_superficial())
print("---------------------------------")
print("Volumen del Cilindro: ", cilindro1.calcular_volumen())
print(f"Area superficial del cilindro:  {cilindro1.calcular_area_superficial}")

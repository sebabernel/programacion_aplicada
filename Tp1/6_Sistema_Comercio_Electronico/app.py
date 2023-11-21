from carritoCompra import CarritoCompras
from cliente import Cliente
from producto import Producto
from tienda import Tienda

# Instanciamos productos
p1 = Producto(2113, "Pasta Dental", "blanco total", 510, 10)
p2 = Producto(2114, "Zapatos", "Hombre, talle 42",3510, 7)
p3 = Producto(2050, "Camisa", "Hombre, talle XL", 510, 5)
p4 = Producto(2223, "Notebook", "Intel i7", 510, 9)

# Instanciamos la clase Clientes
c1 = Cliente("Maria", "Sarmiento 1119", 40000, "maria@gmail.com")
c2 = Cliente("Romina", "Cochabamba 1900", 20000, "romina@gmail.com")
c3 = Cliente("Ruben", "Inclan 4090", 500000, "ruben@gmail.com")
c4 = Cliente("Abel", "Mexico 1203", 550000, "abel@gmail.com")

# Inicializamos la tienda
tienda1 = Tienda()
print("----------------------")

# Agregar los productos en la tienda
tienda1.agregar_surtido(p1)
tienda1.agregar_surtido(p2)
tienda1.agregar_surtido(p3)
tienda1.agregar_surtido(p4)
# Muestra informe de tienda
tienda1.generar_informe()
print("----------------------")
# Cliente agrega productos a carro
c1.agregar_producto(p2)
c1.agregar_producto(p3)
c1.agregar_producto(p2)
c2.agregar_producto(p1)
c2.agregar_producto(p2)
c2.agregar_producto(p4)

# Muestra los carros de los clientes que compraron
print(c1.carrito_compras)
print(c2.carrito_compras)

# Cliente Maria compra productos de un carro
c1.comprar()
# Cliente quita productos de su carro
c2.quitar_producto(p1)

# Se muestra los carros de los clientes despues de las acciones
print(c1.carrito_compras)
print(c2.carrito_compras)

tienda1.generar_informe()
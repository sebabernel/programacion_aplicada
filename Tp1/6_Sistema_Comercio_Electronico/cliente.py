from carritoCompra import CarritoCompras
from producto import Producto
"""Cliente: Una clase que representa a un cliente con atributos como nombre,
dirección, carrito de compra, etc."""

 
class Cliente(Producto):
    
    
    def __init__(self,nombre, direccion, saldo, mail):
      self._nombre = nombre
      self._direccion = direccion
      self._saldo = saldo
      self._mail = mail
      self.carrito_compras= CarritoCompras() # crea campo de compras vacio

    @property
    # Encapsulamos para evitar accesos inadecuados
    def nombre(self):
      return self._nombre
    @property
    def direccion(self):
      return self._direccion
    @property
    def saldo(self):
      return self._saldo
    @property
    def mail(self):
      return self._mail
    
    # Muestra la informacion del cliente
    def __str__(self):
      return f"Cliente: {self._nombre} -- Mail: {self._mail} -- Pagar: {self._saldo:.2f}"
    
    # Metodo para agregar productos al carro del cliente
    def agregar_producto(self, producto):
      self.carrito_compras.agregar_producto(producto)
    
    # Quitar un producto del carro del cliente
    def quitar_producto(self, producto):
      self.carrito_compras.quitar_producto(producto)

    # Vaciar carro de compras
    def vaciar_carro(self):
      self.carrito_compras.vaciar()

    # Comprar los prodcutos del carro de compras
    def comprar(self):
      total = self.carrito_compras.calcular_total()
      if total > self.saldo:
        print("El saldo de su cuenta es insuficiente para la compra")
      else:
        self._saldo -= total
        print(f"Pago realizado, total ${total:.2f}, el saldo en su cuenta es ${self._saldo:.2f}")
        self.vaciar_carro()
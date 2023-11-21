"""Producto: Una clase que representa un producto con atributos como nombre,
precio, cantidad en stock, etc."""

class Producto:

    def __init__(self,id_producto, nombre, descripcion, precio, stock):
        self._id_producto = id_producto
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._stock = stock

    @property
    def id(self):
        return self._id
    @property
    def nombre(self):
        return self._nombre
    @property
    def descripcion(self):
        return self._descripcion
    @property
    def precio(self):
        return self._precio
    @property
    def stock(self):
        return self._stock
    # Mostrar Producto
    def __str__(self):
        return f" Id Producto: {self._id_producto}- {self._nombre}-{self._descripcion}- Precio: {self._precio}- Stock: {self._stock}"
    
    # Reducir la cantidad de producto en uno
    def reducir_cantidad(self): 
        if self._stock > 0:
            self._stock -= 1
    # Aumenta cantidad de producto en uno
    def aumentar_cantidad(self):
        self._stock += 1
    


from producto import Producto

class CarritoCompras(Producto):

    def __init__(self):
        self.productos = []

    # Mostrar los productos del Carro de compras
    def __str__(self):
        if len(self.productos) == 0:
            return "El carro está vacio."
        else:
            resultado = "El carro contiene los siguientes productos:\n"
            for producto in self.productos:
                resultado += str(producto) + "\n"
            return resultado
    # Metodo para agregar producto al carro del cliente
    def agregar_producto(self, producto):
        self.productos.append(producto)
        producto.reducir_cantidad()
        
    # Metodo para quitar un producto del carro del cliente
    def quitar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            producto.aumentar_cantidad()
        else:
            print("El producto no esta en el carro.")
    
    # Metodo para vaciar el carro
    def vaciar(self):
        self.productos = []

    # Metodo para calcular el total a pagar        
    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
            
        return total   

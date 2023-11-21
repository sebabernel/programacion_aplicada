from producto import Producto

class Tienda(Producto):
    def __init__(self):
        self.surtido = []

    # Dar de alta a productos en el surtido de la tienda
    def agregar_surtido(self, producto):
        self.surtido.append(producto)
    
    # Agrega stock al producto por Id_producto
    def agrega_stock(self, id_producto, cantidad):
        for producto in self.surtido:
            if producto.id_producto == id_producto:
                producto.stock += producto.stock + cantidad
                print(f"Producto: {producto.self._nombre} actualizado, nuevo stock {producto.self._stock}")
        return

    # Metodo para venta de Producto
    def venta_producto(self, id_producto, cantidad):
        for producto in self.surtido:
            if producto.id_producto == id_producto:
                if producto._stock >= cantidad:
                    producto.stock -= cantidad
                else:
                    return
    
    # Realiza informe de surtido con stock
    def generar_informe(self):
        texto = ""
        print("id_Producto_______Nombre_______Precio_______Stock")
        for producto in self.surtido:
            texto = f"{producto._id_producto}___________{producto._nombre}_______{producto._precio}_______{producto._stock}"
            print(texto + "\n")
            

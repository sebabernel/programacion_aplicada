from Libro import Libro
from Libreria import Libreria

libro1 = Libro("El Gran Gatsby", "F. Scott Fitzgerald", 10.99)
libro2 = Libro("1984", "Jorge Orwell", 12.99)
libro3 = Libro("Matar a un ruiseñor", "Harper Lee", 9.99)

libreria = Libreria()
libreria.agregar_libro(libro1)
libreria.agregar_libro(libro2)
libreria.agregar_libro(libro3)

precio_total = libreria.calcular_precio_total()
print("----------------------------------------")
print(f"El preckio total de todos los libros ")
print(f"en la Libreria es: ")
print(f"----------------------- u$s {precio_total}")
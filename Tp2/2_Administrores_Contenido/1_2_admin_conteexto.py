""" Hacer un administrador de contexto para notificar eventos al entrar y al  salir de un bloque de código.
Teoria
Para crear un administrador de contexto que notifique eventos al entrar y salir
 de un bloque de código, puedes definir una clase que implemente los métodos
   __enter__ y __exit__. El método __enter__ se ejecuta al entrar en el bloque de código,
     y el método __exit__ se ejecuta al salir del bloque de código."""

class AdministradorContexto:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __enter__(self):
        print(self.mensaje + " - Entrando en el bloque de codigo")
        return self  
    def __exit__(self, tipo_de_excepcion, valor_de_excepcion, traza_de_excepcion):
        print(self.mensaje + " - Saliendo del bloque de codigo")

# se llama al administrador de contextocon with de la siguiente forma
with AdministradorContexto("Administrador de contexto") as ac:
    print("Es es el cuerpo dle administrador de código")
    
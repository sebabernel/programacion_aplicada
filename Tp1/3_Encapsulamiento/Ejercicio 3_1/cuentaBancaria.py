
class CuentaBancaria:
    def __init__(self, titular, saldo = 0):
        self.__titular = titular
        self.__saldo = saldo
    
    # Metodo que accede al saldo y titular
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    def depositar(self, cantidad):
        if cantidad > 0: 
            self.__saldo += cantidad
            return True
        else:
            print("El deposito debe ser mayor que cero.")
            return False
        
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return True
        else:
            print("Saldo insuficiente.")
            return False

    # Metodo que consulta el saldo    
    def consultar_saldo(self):
        print(f"Saldo atual de {self.titular}: {self.saldo}")
    
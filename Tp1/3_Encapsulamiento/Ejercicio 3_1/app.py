from cuentaBancaria import CuentaBancaria

# Crea el objeto cuenta, de la clase Cuenta Bancaria
cuenta = CuentaBancaria("Sebastian Bernel", 1000000)

# Consulta saldo
cuenta.consultar_saldo()

# Deposita Dinero
cuenta.depositar(500)
cuenta.consultar_saldo()

# Retira Dinero
cuenta.retirar(2000)
cuenta.consultar_saldo()


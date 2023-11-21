from coche import Coche

# Instancio el coche
coche = Coche(0, 0)

print(f"Velocidad actual: {coche.velocidad}")
print(f"Kilometraje actual: {coche.kilometraje}")

# Acelerar el coche

coche.acelerar(30)

# Registra el Kilometraje
coche.registrar_kilometraje(30)

print(f"Velocidad actual: {coche.velocidad}")
print(f"Kilometraje actual: {coche.kilometraje}")





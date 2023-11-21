from estudiante import Estudiante

# Creas el objeto estudiante
calificaciones_sebasBernel = [10, 9, 9, 8]
sebasBernel = Estudiante("Sebas", 45, calificaciones_sebasBernel)

# Obtener información protegida
print(f"Nombre: {sebasBernel.nombre} \nEdad: {sebasBernel.edad} \nCalificaciones: {sebasBernel.calificaciones}")

print("-----------------------------------------------------")
# Cambiar calificaciones
nuevas_notas_sebasBernel = [10, 10, 10, 9]
sebasBernel.establecer_calificaciones(nuevas_notas_sebasBernel)
# Imprime actualizacion de notas
print(f"Nombre: {sebasBernel.nombre} \nEdad: {sebasBernel.edad} \nCalificaciones: {sebasBernel.calificaciones}")

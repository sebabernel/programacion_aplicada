"""4.2.   Toma una lista de cadenas y utiliza map con una función lambda para  convertir todas las cadenas en mayúsculas."""

# Creamos la lista
cadenas = ["cadena", "para ", "aprobar", "materia", "con ", "mayusculas"]

# Utilizo map y una funcion lambda para convertira la cadena en mayusculas
cambiar = list(map(lambda x: x.upper(), cadenas))

# Imprimir  la nueva lista
print(cambiar)


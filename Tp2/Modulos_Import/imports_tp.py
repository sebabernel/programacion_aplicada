"""3.1.   Crear dos módulos en el mismo directorio. Desde un módulo, importa  una función o variable del otro utilizando una importación absoluta.
  3.2.   Crear dos módulos en el mismo directorio. Desde un módulo, importa  una función o variable del otro utilizando una importación relativa.
  3.3.   Crear dos módulos en el mismo directorio. Desde un módulo, importar  el otro sin usar from.
  3.4.   Crear dos módulos en el mismo directorio. Desde un módulo, importa  una función o variable del otro utilizando una 
  importación absoluta y  generar un error de importación circular.
  3.5.   Crear dos módulos en el mismo directorio. Desde un módulo, importar  el otro sin usar from y utilizando alias.  
  3.6.   Crear dos módulos en el mismo directorio. Desde un módulo, importa  una función o variable del otro
         utilizando una importación absoluta y  utilizar un alias
  3.7.   Crear dos módulos en el mismo directorio. Desde un módulo, importa  una función o variable
         del otro utilizando una importación relativa y  utilizar un alias"""

# 3.1.
from modulo1 import funcion

print(funcion())

# 3.2.

from . import modulo2
modulo2.funcion2()

#3.3.

import modulo1
 
modulo1.sin_from()

# 3.4.
from modulo1 import funcion

print(funcion())
# Se produce un error de importación circular cuando dos módulos se importan mutuamente
def funcion_circular():
  print("Se produce un error de importación circular cuando dos módulos se importan mutuamente.")

# 3.5.
import modulo1 as mod1
#Se importa el módulo completo, pero se utiliza un alias para referirse a él de una manera más corta
print(mod1.variable_modulo1)
   
# 3.6.

from modulo1 import funcion as func_mod1
#Se importa una función o variable específica del módulo y se le asigna un alias

print(func_mod1())

#3.7. Crear dos módulos en el mismo directorio. Desde un módulo, importa  una función o variable
# del otro utilizando una importación relativa y  utilizar un alias
from .modulo1 import funcion_ImportAlias as func_Alias

print(modulo1.func_Alias)
# Se importa una función o variable específica del módulo
# y se le asigna un alias, utilizando la importación relativa.
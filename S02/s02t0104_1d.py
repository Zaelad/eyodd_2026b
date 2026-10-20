# Importando funcion array
# del modulo array y renombrarlo
# como arr 
from array import array as arr

# Importando una funcion de otro 
# archivo 
from s02t0102_1D import print_array

my_array = arr('i',[2,10,15,20,10])

print("--- ANTES DE LA ELIMINACION ---")
print_array(my_array)

# Eliminacion
try: 
 my_array.remove(100)
except:
  print(f"el elemento no se encunetra en el arreglo")
print("--- DESPUES DE LA ELIMINACION ---")
print_array(my_array)
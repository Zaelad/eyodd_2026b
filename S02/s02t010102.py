# importando el modulo array de la bilbioteca
# array y renombrando arr
from array import array as arr 

def print_array(input):
  print("[",end=" ")
  for element in input:
    print(element,end=',')
print("/b]")

my_array = arr('i',[2,10,15,20])
print_array(my_array)

# buscar el elemnto 15
number_to_search = 15
for integer in my_array:
  counter = 0
  print(f"se busca {number_to_search}en el arreglo.")
  if  integer == number_to_search:
    print("numero encontrado")
    # sirve para terminar el ciclo
    break
  # incrementamos contador
  counter+=1
  if counter == len (my_array):
     print("numero no encontrado")
  
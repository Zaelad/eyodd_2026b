# array
#from array import *
import array as arr 

#creacion de un arreglo
# i: entero con signo
# I: entero sin signo
# f: numero decimal
# d: numero decimal doble
# u: caracter unicode
my_array = arr.array('i',[1,2,3,4,5,6,7,8,9,10,11])

# interaccion automatica
# for num in my_array:
#     print(num)

# acceso individual a los elementos
# print(my_array[0]) # primer elemento
# print(my_array[1]) # segundo elemento
# print(my_array[1]) # tercer elemento

# tamaño de un arreglo
# length
# print(len(my_array))

# interaccion por indices
for i in range(len(my_array)):
 if my_array[i] % 2 == 0:
    print(f"elemento num {i+1}:{my_array[i]}")

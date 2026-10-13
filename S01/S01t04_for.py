"""
Escribir un programa qye calcule
la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa 
calculara la suma del 1 al 100
"""
# Importamos biblioteca time
import time

#funcion que suma los
# primeros "n" numeros naturales
def sum_of_n(n):
    total_sum = 0
    # sumando los "n" numeros
    #Ciclo for 
    for number in range(1,n+1):
     total_sum = total_sum + number
     # Retomando el total de la suma 
    return total_sum

 #Creando una marca de tiempo
#variable para guardar dataset
dataset = []  #[(n,time,sum),(n, time,sum)]

#generando el contenido del dataset
for repetition in range(1,11):
    # tomo el tiempo 1
   timestamp_01 = time.time()

   #sumo los "n" numeros 
   n = repetition * 500 
   result =sum_of_n(n) 

   # tomando el tiempo final
   timestamp_02 = time.time()
   elapsed_time = round ((timestamp_02-timestamp_01)*1e6,2)
    # calculando el tiempoelapsed_time = round ((timestamp_02-timestamp_01) * 1e6,2)

    # agregar la tripleta de los datos al dataset
   dataset.append( (n,elapsed_time,result) )

for tup in dataset:
    print(tup)
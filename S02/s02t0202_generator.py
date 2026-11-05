"""""
generators 

lo generadores son funciones que pueden
pausar su ejecucion

cuando se invoca una funcion generadora
devuelve el objeto (aka iterador)

el codigo dentro de la funcion no se ejecuta
de inmediato, solo se compila

la funcion se ejecuta unicamente cuando
interas sobre el geneador

"""

""
def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

    #se invoc funcion generadora
my_iterator = my_generator()

# se itera manualmente sobre el generador
# print(next(my_iterator)) # imprime 1 
# print(next(my_iterator)) # imprime 2
# print(next(my_iterator)) # imprime 3
# print(next(my_iterator)) # imprime 4

# los iteradores se puede iterar con un for
for value in my_iterator:
  print(value)
from array import array as arr

# parametros de mi cuadricula
rows = 3
columns = 2 * rows - 1

# funcion para imprimir matrix
def print_matrix(input_matrix):
    for row in input_matrix:
      print(list(row))

# creando la reticula 2D
matrix = []
# construyendo el grid
for _ in range(rows):
    new_row = arr('i', [0]* columns)
    matrix.append(new_row)

# validando la construccion del grid
print(f"cantidad de filas: {len(matrix)}")
print(f"cantidad de columnas: {len(matrix[0])}")

# for row in matrix:
#     print(list(row))

# calculando el centro de la primera fila
center = columns // 2 # se hace division entera

# estableciendo el centro en 1 
matrix[0][center] = 1

print_matrix(matrix)

# se calcula el resto de la matrix
# siguiendo la logica del siperpinsky gasket
for rows in range(1,rows):
   for columns in range(0, columns):
    left_upper_cell = 0
    right_uppper_cell = 0

    # si la columna donde estamos es mayor a cero
if columns > 0:
   left_upper_cell = matrix[rows-1],[columns-1]

   # si la columna esta un elemento antes del borde derecho
   if columns< columns - 1:
      right_uppper_cell = matrix[rows-1][columns+1]

# guardar el arreglo
if left_upper_cell != right_uppper_cell:
   matrix[rows][columns] = 1
else:
   matrix[rows][columns] = 0

print()
print_matrix(matrix)
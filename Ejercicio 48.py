# Deber 48
matrix=[]

filas=4
columna=4
for i in range(filas):
    m=int(input("Ingrese los valores en las filas: "))
    matrix.append([m])
    for j in range(columna-1):
        n=int(input("Ingrese los valores en las columnas: "))
        matrix[i].append(n)
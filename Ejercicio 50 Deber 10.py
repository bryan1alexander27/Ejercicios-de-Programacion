# Ejercicio 50, Deber 10
print("Ejercicio de matrices del 4 hasta el 30 en un rango de 50 a 1000")
import random 
while True:
    n=int(input('Ingrese numero de filas deseadas: '))
    m=int(input('Ingrese numero de columnas deseadas: '))
    if n<4 or m<4:
        print('Error')
    if n>30 or m>30:
        print('Error')
    else:
        break
    
matrix=[[int()for i in range(n)] for j in range(m)]
for k in range(n):
    for l in range(m):
        matrix[k][l]=random.randint(50, 1000)

for a in range (n):
    for b in range (m):
        print('|', matrix[a][b], '|', end=' ')
    print('   ')

if n==m:
 print("La diagonal principal: ")
 print()
    
for r in range (n):
     for s in range (m):
         if r==s:
             print("/",matrix[r][s],"/", end=" ")
         else:
          print("/","- ","/",end=" ")
     print("")
     print()
         
if n==m:
 print("La diagonal secundaria: ")
 print()
 
for t in range (n):
     for u in range (m):
      if t+u==n-1:
       print("/",matrix[t][u],"/",end=" ")
      else:
       print("/","- ","/",end=" ")
     print("")
print("Final del programa")
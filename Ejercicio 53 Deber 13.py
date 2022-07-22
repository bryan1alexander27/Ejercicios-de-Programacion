# Bryan Titoaña
# 2do Nivel
# 21/07/2022

print("Inicio del programa")
import random
def imprimir(matrix):
	print("\tC1    C2    C3    C4    C5    C6    C7    TOTAL")
	for k in range(11):
		if k==10:
			print("TOTAL",end="   ")
		else:
			print("F",k+1,end="\t")
		for l in range(8):
			if k==10:
				print(matrix[k][l],end="  ")
			else:
				if matrix[k][l]<10:
					print(matrix[k][l],end="     ")
				elif matrix[k][l]==100:
					print(matrix[k][l],end="   ")
				else:
					print(matrix[k][l], end="    ")
		print("")
        
def llenar(matrix):
	for p in range(11):
		matrix.append([])
		for q in range(8):
				if p==10:
					matrix[p].append(0)
				elif q==7:
					matrix[p].append(0)
				else:
					matrix[p].append(random.randint(0,100))

def Mayor_materia(matrix):
	mayor=0
	materia=0
	for r in range(10):
		if (matrix[r][7]>mayor):
			mayor=matrix[r][7]
			materia=r
	print("LA MATERIA QUE POSEE EL MEJOR PROMEDIO ES F",materia+1,"CON PROMEDIO DE ",mayor)
		
def Menor_materia(matrix,opciones):
	for s in range(10):
		if(matrix[s][7]<matrix[10][7]):
			if opciones==1:
				print("LA MATERIAS MAS BAJAS SON F",s+1)
			else:
				print("LAS MATERIAS F",s+1,"CON UN PROMEDIO DE ",matrix[s][7])

def total(matrix):
	for t in range(10):
		suma=0
		for u in range(7):
			suma=suma+matrix[t][u]
		matrix[t][7]=round(suma/7,2)
	
	for v in range(8):
		suma=0
		for w in range(11):
			suma=suma+matrix[w][v]
		matrix[10][v]=round(suma/10,2)
				
			
matrix=[]
llenar(matrix)
total(matrix)
print("NOTAS GENERADAS ALEATORIAMENTE EN LA SIGUIENTE TABLA: ")
imprimir(matrix)
print("MENU")
print("1.LA MATERIA CON LAS PEORES CALIFICACIONES MENORES AL PROMEDIO: ")
print("2.LA NOTA DE TODAS LAS MATERIAS CON PEORES CALIFICACIONES: ")
print("3.LAS MATERIAS CON LAS MEJORES CALIFICACIONES")
opcion=int(input("INGRESE UNA DE LAS TRES OPCIONES PRESENTADAS: "))
if opcion==1:
	Menor_materia(matrix,opcion)
elif opcion==2:
	Menor_materia(matrix,opcion)
elif opcion==3:
	Mayor_materia(matrix)
else:
	print("LA OPCION SELECCIONADA NO EXISTE, LO SIENTO MUCHO")
print("Final del programa")
			

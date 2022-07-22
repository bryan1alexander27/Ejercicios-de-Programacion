# Bryan Titoaña
# 2do Nivel
# 21/07/2022

print("Inicio del programa")

import random
def imprimir(matrix,n):
	for k in range(n+1):
		print(" ",end="")
		for l in range(n+1):
			if l==n:
                
				print("TOTAL",matrix[k][l],end="  ")
			elif k==n:
				print("TOTAL",matrix[k][l],end="  \t ")
			else:
				if matrix[k][l]<10:
					print(matrix[k][l],end="   \t\t  ")
				elif matrix[k][l]==100:
					print(matrix[k][l],end=" \t\t  ")
				else:
					print(matrix[k][l], end="\t  \t  ")
		print("")
		
def llenar(matrix,m):
	for p in range(m+1):
		matrix.append([])
		for q in range(m+1):
            
				if p==m:
					matrix[p].append(0)
				elif q==m:
					matrix[p].append(0)
				else:
					matrix[p].append(random.randint(0,100))

def validacion(numero):
	if numero>=4 and numero<=30:
        
		print("EL VALOR ES CORRECTO, SE ENCUENTRA EN EL RANGO CORRESPONDIDO.")
		return True
	else:
		print("ERROR, EL VALOR NO SE ENCUENTRA EN EL RANGO CORRESPONDIDO.")
		return False
					
def total(matrix,m):
	for r in range(m):
		sumar=0
		for s in range(m):
			sumar=sumar+matrix[r][s]
		matrix[r][m]=round(sumar/m,2)
	for i in range(m+1):
		sumar=0
		for j in range(m+1):
			sumar=sumar+matrix[j][i]
		matrix[m][i]=round(sumar/m,2)


m=int(input("INGRESE EL VALOR DESEADO: "))

if validacion(m)==True:
    
	matrix=[]
    
	llenar(matrix,m)
    
	total(matrix,m)
    
	imprimir(matrix,m)
    
print("Final del programa")
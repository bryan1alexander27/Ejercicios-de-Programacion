# Bryan Titoaña
# 2do Nivel
# 21/07/2022
k=0
l=0
print("Inicio del programa")
import random
def validar(numero):
	if numero>=4 and numero<=30:
		print("EL VALOR INGRESADO ES CORRECTO,SE ENCUENTRA ENTRE EL 4 Y 30")
		return True
	else:
		print("ERROR, EL VALOR INGRESADO NO SE ENCUENTRA ENTRE EL 4 Y 30")
		return False
		
def primo(numero2):
	for p in range(2,numero2):
		if numero2%p== 0:
			return False
	return True

def llenar(vectores_primos,m,vectores):
	for k in range (m-1):
		vector.append(random.randint(0,100))
	print("EL VECTOR RANDOM OBTENIDO ES: ")
	for l in range (m):
		print(vector[l])
		if primo(vector[l])==True:
			vectores_primos.append(vector[l])
	
valor=int(input("INGRESE EL VALOR DESEADO: "))
if validar(valor)==True:
	vectores_primos2=[]
	vector=[valor]
	llenar(vector,valor,vectores_primos2)
	if len(vectores_primos2)==0:
		print("ERROR, NO SE REGISTRAN NUMERO PRIMOS")
	else:
		i=0
		print("LOS NUMERO PRIMOS DEL VALOR INTRODUCIDO SON: ")
		for i in range(len(vectores_primos2)):
			print(vectores_primos2[i])
print("Final del programa")
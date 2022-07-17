#Bryan Titoaña
#2do Nivel
#28/06/22
print("Inicio del programa")
cantidad=int(input("Dimension del vector: "))
mayor=0
menor=0
i=1
from time import sleep
lista=[]
import random
while(cantidad > 0):
    numero=random.randint(50,100)
    lista.append(numero)
    sleep(1)
    i=1+1
    cantidad=cantidad-1
    print(lista)
mayor=max(lista)
menor=min(lista)
for i in range(len(lista)-1):
    for j in range(len(lista)-1):
        print("El valor de la posicion es: ",lista[j], "con",lista[j+1])
        if lista[j]>lista[j+1]:
            temporal=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=temporal
            print("Intercambiando posiciones de: ",lista[j], "por",lista[j+1])
print(lista)
sleep(1)
print("Final del programa")


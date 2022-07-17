# Ejercicio 2 
# Nivel: 2do Nivel
# Fecha: 17/06/2022
print("Inicio del programa")
num1=0#Num1 es numero 1
d1=0# d1 es division
def isPrime(num1):
    d1=2
    while d1<num1:
        if num1%d1==0:
            return False
        d1+=1
    return True
for i in range(1,20):
    if isPrime(i+1):
        print(i+1,end="")
print()
print("Final del programa")
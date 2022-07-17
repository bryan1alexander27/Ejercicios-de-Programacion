#Ejercicio 10
while True:
    num1=int(input("Digitar el primer numero: "))
    num2=int(input("Digitar el segundo numero: "))
    if num1==num2:
        print("Error los numeros son iguales")
    else:
        break
if num1>num2:
    minimo=num2
    maximo=num1
else:
    minimo=num1
    maximo=num2
while True:
    numero=int(input("Digite un numero: "))
    if numero==0:
        break
    else:
        print("Puedo continuar")
        



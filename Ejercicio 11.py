#Ejercicio 11
numero=1
sumainter=0
contador1=0
suma1=0
contador2=0
while True:
    num1=int(input("Digitar el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
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
while numero!=0:
    numero=int(input("Digite un numero: "))
    if numero>minimo and numero<maximo:
        sumainter+=numero
    elif numero<minimo or numero>maximo:
        suma1+=numero
        contador1+=1
    elif numero==minimo or numero == maximo:
        contador2+=1
print("La suma de los numeros que estan dentro es: ",sumainter)
print("El promedio de los numeros fuera del intervalo es: ",suma1/contador1)
print("La cantidad de numeros ingresados iguales a los limites de intervaos son: ",contador2)
print("Fin del programa")
    

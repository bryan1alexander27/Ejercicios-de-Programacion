#Ejercico de programacion:
#Bryan Titoaña
contadorimpar=0 #El contador de la variable impar es igual a cero
contadorpar=0 #El contador de la variable par es igual a cero
contador5=0 #El contador de la variable 5 es igual acero
contador3=0 #El contador de la variable 3 es igual a cero
suma=0 #Indica la suma es igual a cero
num2=int(input("Ingrese numero de columnas de la tabla de multiplación: ")) #Escribe ingrese numero de columnas de la tabla de multiplicar.
num1=int(input("Ingrese numero de tablas de multiplicación deseadas: ")) #Escribe el numero de tablas de multiplicacion deseadas.
for i in range(1,num1+1): #Para i dentro del rango 1, num1 mas 1.
    contadorpar=0 #El contador de la variable par es igual a cero.
    contadorimpar=0 #El contador de la variable impar es igual acero.
    contador5=0 #El contador de la variable 5 es igual a cero
    contador3=0 #El contador de la variable 3 es igual a cero.
    print("La tabla del numero",i,"es: ") #Se imprime las tablas de multiplicar
    print('\n') # Se imprime un salto de linea
    for j in range(1,num2+1): #Para j en el rango 1, num2 mas 1
        resultado=j*i #La variable resultado asigna j multiplicado por i.
        if(resultado%5)==0:#Si el contador es igual a cero
           contador5+=1 #El contador 5 suma 1
        if(resultado%3)==0:#Si el contador es igual a cero
           contador3+=1 #El contador 3 suma 1
        if(resultado%2)==0: #Si el resultado es igual a cero
           contadorpar+=1 #El contador par suma 1
        else:#Si no
            contadorimpar+=1 #El contador impar suma 1
        suma+=resultado #La suma es igual a la variable suma mas el resultado
        print(i,'x',j,'=',resultado) #Se imprime una multiplicacion entre el multiplicador y sus numeros a multiplicar
    print('\n') #Se imprime un salto de linea
    print("La suma de los numeros es: ",suma) #Escribe la suma de los numeros
    print("El promedio de la suma es: ",suma/15) # Escribe el promedio de la suma
    print("Los multiplos del 3 son: ",contador3) #Escribe los multiplos del 3
    print("Los multiplos del 5 son: ",contador5) #Escribe los multiplos del 5
    print("La cantidad de numeros pares son: ",contadorpar) #Escribe la cantidad de numeros pares
    print("La cantidad de numeros impares son: ",contadorimpar) #Escribe la cantidad de numeros impares
    print('\n') #Se imprime un salto de linea
       
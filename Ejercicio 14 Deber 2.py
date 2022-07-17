#Deber de programacion:
#Bryan Titoaña
num1=0 # Se define la variable num1 es igual a cero
while(num1<2 or num1>99):#Mientras num1 sea menor de 2 o num1 sea mayor a 99 entonces:
    num1=int(input("Ingrese el valor hasta el cual desea ejecutar: "))#Solicita el ingreso de un valor hasta el cual se desea ejecutar
    if (num1<2 or num1>99): #Si num1 es menor a 2 o num1 es mayor a 99 entonces
        print("Introduzca un numero, este debe ser mayor de 2 y menor de 100")#Imprime un numemero el cual debe ser mayor de 2 y menor que 100
i=1 #La variable i es igual a 1
while(i<num1+1):#Mientras i sea menor a num1+1
    contadorpar=0 #El contador de la variable par es igual a cero.
    contadorimpar=0 #El contador de la variable impar es igual acero.
    contador5=0 #El contador de la variable 5 es igual a cero
    contador3=0 #El contador de la variable 3 es igual a cero.
    suma=0#El contador de la suma es igual a cero
    print("La tabla del numero",i,"es: ")# Imprime la tabla del numero i es:
    j=1 #La variable j es igual a 1
    while(j<16):#Mientras j sea menor a 16
        resultado=i*j#La variable resultado es igual a i multiplicado pot j
        if (resultado%5)==0:#Si e contador es igual a cero
            contador5+=1 #El contador 5 suma 1
        if(resultado%3)==0:#Si el contador es igual a cero
            contador3+=1 #El contador 3 suma 1
        if(resultado%2)==0: #Si el resultado es igual a cero
            contadorpar+=1 #El contador par suma 1
        else:#Si no
            contadorimpar+=1 #El contador impar suma 1
        suma+=resultado #La suma es igual a la variable suma mas el resultado
        print(i,'x',j,'=',resultado) #Se imprime una multiplicacion entre el multiplicador y sus numeros a multiplicar
        j+=1 #La variable contable j es igual a la misma variable mas 1
    print("La suma de los numeros es: ",suma) #Escribe la suma de los numeros
    print("El promedio de la suma es: ",suma/15) # Escribe el promedio de la suma
    print("Los multiplos del 3 son: ",contador3) #Escribe los mulriplos del 3
    print("Los multiplos del 5 son: ",contador5) #Escribe los multiplos del 5
    print("La cantidad de numeros pares son: ",contadorpar) #Escribe la cantidad de numeros pares
    print("La cantidad de numeros impares son: ",contadorimpar) #Escribe la cantidad de numeros impares
    i+=1 #La variable contable i es igual a la misma variable mas 1
print("Fin del programa")# Imprime fin del programa

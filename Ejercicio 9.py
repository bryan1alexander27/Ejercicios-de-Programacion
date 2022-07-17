# Ejercicio 9
contador=0
contador_igual=0
contador_negativo=0
while True:
    while True:
        num1=int(input("Ingrese el numero uno: "))
        num2=int(input("Ingrese el numero dos: "))
        if num1==num2:
            print("Error los numeros no deben ser iguales")
            contador_igual+=1
        elif num1<0 or num2<0:
            contador_negativo+=1
            print("Error los numeros no deben ser negativos")
        else:
            break
    print("Las veces que se a ejecutado el codigo es: ",contador)
    print("Las veces que se digitaron numeros iguales es: ",contador_igual)
    print("Las veces que digitaron numeros negativos es: ",contador_negativo)
    salir=input("Para salir,digite si:")
    if salir=='si'or salir=='SI'or salir=='sI'or salir=='Si':
        break
    


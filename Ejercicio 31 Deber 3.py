#Ejercicio 1 
#2do Nivel
#Fecha:17/06/2022
print("Inicio del Programa")
l1=0 #l1 es igual a litros
m1=0 #m1 es igual a millas
g1=0 #g1 es igual a galon
km=0 #km es igual a kilometro
def l100kmtompg(l1):
    g1=l1/3.785411784
    m1=100*1000/1609.344
    return m1/g1
def mpgtol100km(m1):
    km=m1*1609.344/1000
    l1=3.7851411784
    kilometros100=km/100
    return l1/kilometros100
print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
print("Final del programa")


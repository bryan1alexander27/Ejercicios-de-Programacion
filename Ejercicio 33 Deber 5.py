# Ejercicio 1 
# Fecha:21/06/2022
# Nivel: Segundo Nivel
d1=0 #Dias del mes
año=0 #Indica el año
print("Inicio del programa")
def isYearLeap(año):
    if año<1582:
        return False
    elif año%100!=0:
        return True
    elif año%4!=0:
        return False
    elif año%400!=0:
        return False
    else:
        return True
def daysInMonth(año, mes):
    d1=[31,28,31,30,31,30,31,31,30,31,30,31]
    if isYearLeap(año) and mes==2:
        return 29
    return d1[mes-1]
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    mo=testMonths[i]
    yr=testYears[i]
    print(yr, mo, '->', end='')
    result=daysInMonth(yr, mo)
    if result==testResults[i]:
        print('OK')
    else:
        print('Fallo')
print("Final del programa")
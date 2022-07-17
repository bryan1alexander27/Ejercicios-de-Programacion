# Nombre: Bryan Titoaña
# Fecha: 21/06/2022
# Nivel: 2do Nivel
print("Inicio del programa")
def isYearLeap(año):
    if año<1582:
        return False
    elif año%4!=0:
        return False
    elif año%400!=0:
        return False
    elif año%100!=0:
        return True
    else:
        return True
def daysInMonth(año,mes):
    monthDays=[31,28,31,30,31,30,31,31,30,31,30,31]
    if isYearLeap(año) and mes==2:
        return 29
    return monthDays[mes-1]
def dayOfYear(año,mes,dia):
    if año<1582:
        return None
    if mes>12 or mes<1:
        return None
    if dia>daysInMonth(año,mes) or dia<1:
        return None
    diastotales=dia
    mes=mes-1
    while mes>0:
        diastotales+=daysInMonth(año,mes)
        mes-=1
    return diastotales
print(dayOfYear(2000,12,31))
print("Final del prograam")
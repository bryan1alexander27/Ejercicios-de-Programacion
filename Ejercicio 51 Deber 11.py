# Ejericio 51 Bryan Titoaña
print('Inicio del programa')
def validar(nombre, edad, cedula, email):
    if '@' in email:
        if str(nombre):
            for cedula in range(1, 10):
                if edad>0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
print(validar('Bryan Titoaña', 18, 3050466865, 'btitoana@est.ups.edu.ec'))
print('Fin del programa')
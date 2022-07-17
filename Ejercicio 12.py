# Ejercicio 12
i=1
mult=0
tabla=0
acu=0
for m in range (1,15+1):
    tabla=tabla+1
    print("Tabla de ",tabla)
    for i in range (1,15+1):
        mult=i*tabla
        acu=acu+mult
        print(tabla,"*",i,"=",mult)
        i=i+1
    print("la suma de la tabla ",tabla, "=",acu)
    print()

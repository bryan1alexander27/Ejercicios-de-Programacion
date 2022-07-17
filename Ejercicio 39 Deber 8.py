# Ejercicio 39
vector1=[7,15,9,22,17,19,26,29,28,30]
vector2=[7,15,9,22,17,19,26,29,28,30]
vector3=[0]*10
for i in range(10):
    vector3[i]=vector1[i]+vector2[i]
    print(vector3[i], end=' ')
print('\n')
for i in range(10):
    vector3[i]=vector1[i]-vector2[i]
    print(vector3[i], end=' ')
print('\n')
for i in range(10):
    vector3[i]=vector1[i]*vector2[i]
    print(vector3[i], end=' ')
print('\n')
for i in range(10):
    vector3[i]=vector1[i]/vector2[i]
    print(vector3[i], end=' ')
def vector(n):
    vector1=[]
    for i in range(len(n)):
    vector3=[]
        vector.append(randint(5,100))
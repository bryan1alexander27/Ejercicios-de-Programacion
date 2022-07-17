#Ejercicio 29
from turtle import *
color('red', 'yelow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) <1:
        break
    end_fill()
    done()



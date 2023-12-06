# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
import random

lista = []

for i in range(10):
    lista.append(random.randint(0,10))

for num in lista:
    print("elemento:", num)
    print("cuadrado:", num**2)
    print("cubo:", num**3)
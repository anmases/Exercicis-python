# Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en uno de estos estados:
#•	exteriores
#•	tangentes exteriores
#•	secantes
#•	tangentes interiores
#•	interiores
#•	concéntricas

import math

x1 = float(input("introduce la cordenada x del punto central de la 1º circunferencia: "))
y1 = float(input("introduce la cordenada y del punto central de la 1º circunferencia: "))
r1 = float(input("introduce el radio r de la 1º circunferencia: "))
x2 = float(input("introduce la cordenada x del punto central de la 2º circunferencia: "))
y2 = float(input("introduce la cordenada y del punto central de la 2º circunferencia: "))
r2 = float(input("introduce el radio r de la 2º circunferencia: "))

distancia = math.sqrt(pow(x1+x2, 2)+pow(y1+y2, 2)) #calculamos la distancia entre centros con Tª de pitágoras.

if x1 == x2 and y1 == y2:
    #Si sus centros coinciden, son concéntricas
    print("son concéntricas")
if r1+r2 < distancia:
    #Si la suma de sus radios es menor que su distancia entre centros, es exterior
    print("son exteriores")
if max(r1, r2) > distancia:
    #Si la distancia entre centros es menor que el mayor de los radios, una está dentro de la otra
    print("son interiores")
if r1+r2 == distancia:
    #Si la suma de los radios es igual a la distancia entre centros, son tangentes exteriores
    print("son tangentes exteriores")
if r1-r2 == distancia:
    #Si la distancia entre centros es igual a la distancia entre centros, son tangentes interiores
    print("son tangentes interiores")
if r2+r2 > distancia:
    #Si la suma de los radios es mayor a la distancia entre centros, son secantes
    print("son secantes")

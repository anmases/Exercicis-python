# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).

lista = []

while(True):
    num = int(input("numero:"))
    if(num < 0): break
    else: lista.append(num)

print(lista)
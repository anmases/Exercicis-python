#Se pueden recorrer listas con for. Su estructura básica es for i in lista:

#Se pueden generar secuencias de números con range()
#range(n): genera una secuencia desde 0 hasta n-1
#range(n, m): genera una secuencia desde n hasta m-1
#range(n, m, k): genera una secuencia desde n hasta m-1 saltando de k en k

for i in range(20, 0, -1):
    print(i)

#imprime del 0 al 10 de 2 en 2
for i in range(0, 11, 2):
    print(i)

#Se puede añadir un contador o un acumulador externo:
cont=0
for i in range(0, 20):
    cont+=1
    print(cont)
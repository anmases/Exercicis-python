# Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

diccionario = {}
numero = int(input("numero:"))

for i in range(numero+1):
    diccionario[i] = i**2

print(diccionario)
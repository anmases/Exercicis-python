#Recogida de datos:
print("---------------------Análisis de datos------------------------")
print("Introduce todos los números que desee analizar (introduzca 0 o negativo para salir)")

numeros = []
try:
    while(3>2):
        numero = int(input())
        if(numero != 0):
            numeros.append(numero)
        else: break
except:
    print("el valor introducido no es un número")


#Aquí va la parte análisis del array de números, en caso de provenir de una fuente de datos externa.

print("máximo:", max(numeros))
print("mínimo:", min(numeros))
print("suma:", sum(numeros))
print("Lista ordenada de menor a mayor:", sorted(numeros))


    
       
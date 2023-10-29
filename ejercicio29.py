# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))

# Ordenar los números de mayor a menor usando condicionales
if num1 >= num2 and num1 >= num3:
    # num1 es el mayor
    if num2 >= num3:
        # num2 es el segundo mayor y num3 es el menor
        print(num1, num2, num3)
    else:
        # num3 es el segundo mayor y num2 es el menor
        print(num1, num3, num2)
elif num2 >= num1 and num2 >= num3:
    # num2 es el mayor
    if num1 >= num3:
        # num1 es el segundo mayor y num3 es el menor
        print(num2, num1, num3)
    else:
        # num3 es el segundo mayor y num1 es el menor
        print(num2, num3, num1)
else:
    # num3 es el mayor
    if num1 >= num2:
        # num1 es el segundo mayor y num2 es el menor
        print(num3, num1, num2)
    else:
        # num2 es el segundo mayor y num1 es el menor
        print(num3, num2, num1)

###############################  Método 2   #################################

mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)
mediano = (num1 + num2 + num3) - mayor - menor
print(mayor, mediano, menor)

############################### Método 3 #####################################

vector = [num1, num2, num3]
vector.sort(reverse = True) #con true revertimos el orden para que sea descendiente
print(vector[0], vector[1], vector[2])

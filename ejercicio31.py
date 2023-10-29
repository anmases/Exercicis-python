# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
#•	Si se cumple Pitágoras entonces es triángulo rectángulo
#•	Si sólo dos lados del triángulo son iguales entonces es isósceles.
#•	Si los 3 lados son iguales entonces es equilátero.
#•	Si no se cumple ninguna de las condiciones anteriores, es escaleno.

print("introduzca los 3 lados de un triángulo")
l1 = int(input())
l2 = int(input())
l3 = int(input())

if l1 == l2 == l3:
    print("es equilátero")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("es isósceles")
else:
    print("es escaleno")

hipotenusa = max(l1, l2, l3)
c1 = min(l1, l2, l3)
lista = list([l1, l2, l3])
lista.remove(hipotenusa)
lista.remove(c1)
c2 = lista[0]

if pow(hipotenusa, 2) == (pow(c1, 2) + pow(c2, 2)):
    print("es rectángulo")
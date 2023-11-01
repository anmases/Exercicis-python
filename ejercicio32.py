# Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

anyo = int(input("Escriba un año: "))

if anyo % 4 == 0:
    if anyo % 100 != 0 or anyo % 400 == 0:
            print("Es bisiesto")
    else:
            print("no es bisiesto")
else:
    print("no es bisiesto")
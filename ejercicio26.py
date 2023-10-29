# Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

cadena = input("introduce un texto: ")

if cadena.isupper():
    print("Está en mayúscula")
else:
    print("Está en minúscula")
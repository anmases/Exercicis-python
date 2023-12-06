# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.

cadena = input("cadena: ")
mapa = {}
for char in cadena:
    mapa[char] = cadena.count(char)

print(mapa)
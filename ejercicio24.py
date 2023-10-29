# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

dividendo = int(input("introduce el dividendo: "))
divisor = int(input("introduce el divisor: "))

if divisor != 0:
    print("resultado:", dividendo/divisor)
else:
    print("¡¡¡¡No se puede dividir por 0!!!!")
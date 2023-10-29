# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

user = input("introduce el nombre de usuario: ")
password = input("introduce la contraseña: ")

if user == "pepe" and password == "asdasd":
    print("has entrado en el sistema")
else:
    print("Nombre de usuario o contraseña erroneos")
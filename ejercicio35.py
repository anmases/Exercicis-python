# El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
# Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.

alumnos = int(input("Alumnos: "))

if alumnos >= 100:
    print("se deberán pagar:", 65 * alumnos)
elif 99>= alumnos >= 50:
    print("se deberán pagar:", 70 * alumnos)
elif 49>= alumnos >= 30:
    print("se deberán pagar:", 95 * alumnos)
else:
    print("se deberán pagar:", 4000)
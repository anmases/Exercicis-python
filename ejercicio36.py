# La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
# Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

minutos = int(input("minutos: "))
dia = input("Día de la semana: ")
hora = input("hora del día")

total = 0
if minutos < 5:
    total = minutos
elif 5 < minutos < 8:
    total = 5 + (minutos-5)*0.8
elif 8 < minutos < 10:
    total = 5 + 3*0.8 + (minutos-8)*0.7
else:
    total = 5 + 3*0.8 + 2*0.7 + (minutos-10)*0.5

if dia == "domingo" or "Domingo" or "DOMINGO":
    total = total + total*0.03
else:
    if 0 < hora < 12:
        total = total + total*0.15
    else:
        total = total + total*0.1

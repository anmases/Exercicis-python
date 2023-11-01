

total = float(input("total a pagar: "))
salida = "Han entregado "

#Python permite devolver varios valores en una función.
def entrega (moneda, importe, salida):
    billetes = input("Billetes de " + str(moneda) + ": ")
    importe -= int(billetes)*500
    salida += billetes + "de billetes de "+ str(moneda)
    return importe, salida


total, salida = entrega(500, total, salida)
total, salida = entrega(200, total, salida)
total, salida = entrega(100, total, salida)
total, salida = entrega(50, total, salida)
total, salida = entrega(20, total, salida)
total, salida = entrega(10, total, salida)
total, salida = entrega(5, total, salida)
total, salida = entrega(2, total, salida)
total, salida = entrega(1, total, salida)
total, salida = entrega(0.5, total, salida)
total, salida = entrega(0.2, total, salida)
total, salida = entrega(0.1, total, salida)
total, salida = entrega(0.05, total, salida)
total, salida = entrega(0.02, total, salida)
total, salida = entrega(0.01, total, salida)



if total <0:
    print("le toca devolver: ", -total )
else:
    print("le toca pagar: ", total )

print(salida)




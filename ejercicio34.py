# La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
# se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

tipo = input("Tipo [A/B]")
tamanyo = int(input("Tamaño [1,2]"))

if tipo == 'A':
    if tamanyo == 1:
        print("ganancia:", 0.20)
    elif tamanyo == 2:
        print("ganancia:", 0.30)
    else:
        print("La opción no es correcta")
elif tipo == 'B':
    if tamanyo == 1:
        print("ganancia:", -0.30)
    elif tamanyo == 2:
        print("ganancia:", -0.50)
    else:
        print("La opción no es correcta")
else:
    print("la opción introducida no es correcta")


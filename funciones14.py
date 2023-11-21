
def longitudPila(pila):
    if isinstance(pila, list):
        return len(pila)
    else:
        print("el objeto no es una lista")

def estaVaciaPila(pila):
    if len(pila) == 0:
        return True
    else:
        return False
    
def estaLlenaPila(pila):
    if len(pila) != 0:
        return True
    else:
        return False
    
def addPila(cadena, pila):
    if estaVaciaPila(pila):
        pila.append(cadena)
    else:
        print("Error, la pila está llena")

def sacarDeLaPila(pila):
    if estaLlenaPila(pila):
        return pila.pop()
    else:
        print("Error: la pila está vacía")

def escribirPila(pila):
    if estaLlenaPila:
        for item in pila:
            print(item)
    else:
        print("la pila está vacía")


pila = []
while True:
    opcion = int(input("1	Añadir elemento a la pila\n2	Sacar elemento de la pila\n3	Longitud de la pila\n4	Mostrar pila\n5	Salir\n"))
    if opcion == 1:
        addPila(str(input("elemento:")), pila)
        continue
    elif opcion == 2:
        sacarDeLaPila(pila)
        continue
    elif opcion == 3:
        print(str(longitudPila(pila)))
        continue
    elif opcion == 4:
        escribirPila(pila)
        continue
    elif opcion == 5:
        exit()
    else:
        print("La opción introduducida no es correcta")
    
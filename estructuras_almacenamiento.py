#Los arrays no existen en python (los que son de tamaño fijo y de tipo homogéneo).

#########################Listas############################ 
#Existen las listas que son redimensionables y se pueden añadir distintos tipos.

lista = ['a', 3.5, True]
lista1 = [1, 2, 3, 4]
lista2 = ['a', 'b', 'c', 'd']
#Se pueden recorrer al mismo tiempo con zip:
for num, letra in zip(lista1, lista2):
    print(num, letra)

#pertenencia:
2 not in lista1

# Se puede crear un subconjunto:
lista2[1: 3: -1]

min(lista1)
max(lista1)
sum(lista1)
len(lista1)
sorted(lista1)

#Las listas son mutables (no se crea una nueva lista):
lista1[1] = 4
lista1.append(8)

#Copiar la lista:
listaCopia = lista2[:]

#Métodos:
lista1.append(3) #Añade un número al final de la lista
lista1.insert(2, 100) #inserta el 100 en la posición 2, a diferencia de lista[2]=100, que sustituye el que está en esa posición.
lista1.extend(lista2) #Concatena dos listas.
lista1.pop(2) #Es lo contrario de insert, devuelve el elemento indicado y lo devuelve. si no se indica nada elimina el último.
lista1.remove(4) #Elimina el elemento de la posición 4 pero no devuelve nada.
lista1.count(3) #Devuelve el número de apariciones de un elemento de la lista.
lista1.reverse() #Pone la lista del revés.
lista1.sort() #ordena los elementos
lista1.index(5) #nos devuelve el índice donde aparece el primer elemento que le indiquemos

###############################Tuplas############################
#Son inmutables. Una vez creada no se pueden modificar sus elementos ni tampoco su tamaño. Admite diferentes tipos de dato.
tupla = (1, 'hola', False, None)

#métodos:
tupla.count(True)
tupla.index('a')
#operadores in o not in
#operadores sum, min, max, len, sorted
tupla[1: 2: -1] #suconjunto
#operadores concatenación o repetición + o *

#############################Diccionarios#####################
#Son mapas que se definen por conjuntos clave-valor. Su tipado es dinámico, por lo que pueden ser objetos json.

mapa = {"a": 1, "b":2, "c": 3}
mapa['a'] = 5 #Son mutables. Se puede acceder a un valor con la clave.

len(mapa) #devuelve el número de entradas en el mapa.
del(mapa['a']) #Elimina un elemento del mapa.
mapa2 = mapa.copy() #hace una copia del mapa.
mapa.clear() #Elimina todos los elementos de un diccionario.
mapa.update(mapa2) #Nos permite añadir al mapa los elementos de otro mapa.
mapa.get("a", "no existe") #nos devuelve el elemento de la clave indicada. Si no existe devuelve el mensaje.
mapa.pop("a") #Saca un elemento del diccionario y lo devuelve.
mapa.keys() #nos devuelve una lista con las claves del diccionario, lo que nos permite recorrerlo
mapa.values() #nos devuelve una lista con los valores del diccionario.
mapa.items() #nos devuelve una lista con los elementos clave + valor del diccionario. como una lista de tuplas (clave, valor)

for i in mapa.keys:
    print(mapa[i]) #imprime los valores según la clave.

#Se pueden recorrer simultáneamente:
for clave,valor in mapa.items():
    print(clave, "->", valor)

###############################Conjuntos###################################
#Son una colección de elementos que, a diferencia de una lista, no admite duplicados, y además están desordenados.
#Son mutables en tamaño (redimensionables), pero no se pueden cambiar los que ya están dentro. Son de tipo heterogeneo
#Se definen como un mapa, pero de elementos únicos, o con la clase set()

conjunto1 = {1, 2, True, 'a'}
conjunto2 = set(['a','b', 3])

conjunto1.add(False) #Añade un elemento al conjunto. Si ya se encuentra no lo añade.
conjunto1.update(conjunto2) #Añade los elementos de un conjunto a otro conjunto.
conjunto1.remove(1) #Elimina el elemento que esté en el conjunto. Si no está dará un error.
conjunto1.discard(1) #Elimina el elemento que está en el conjunto, pero no dará ningún error si no está.
conjunto1.pop() #Elimina un elemento aleatorio del conjunto.
conjunto1.clear() #Elimina todos los elementos del conjunto.
conjuntoCopia = conjunto1.copy() #hace una copia del conjunto.
conjunto1.union(conjunto2) #También se puede usar | y devuelve un nuevo conjunto que incluya a todos los de ambos.
conjunto1.intersection(conjunto2) #También se puede usar & y devuelve un conjunto solo con los que están en ambos.
conjunto1.difference(conjunto2) #también se puede usar - y devuelve un conjunto y que no están en los otros.
conjunto1.symmetric_difference #Actualiza el conjunto con la diferencia simétrica del otro conjunto.
conjunto1.isdisjoint(conjuntoCopia) #Comprueba si NO existen elementos comunes.
conjunto1.issubset(conjunto2) #Comprueba si todos los elementos del conjunto están en el otro conjunto.
conjunto1.issuperset(conjunto2) #comprueba si el segundo conjunto contiene todos los elementos del primero.



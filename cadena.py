cadena = "Hola Mundo"

subcadena = cadena[2: 7: -1] #Esto es para generar una subcadena, de la posición 2 hasta la 7 en sentido inverso [inicio, fin, salto]

cadena = str(3.28) #Esto es para castear cualquier tipo a string.

#Si creamos un string, estamos creando una instancia de la clase string, que tiene sus métodos, como upper()
#Los strings son inmutables, no se puede alterar su contenido. Si se usa un método que lo altera, en realidad se está creando una nueva instancia.

cadena[2] = 'x' #Esto daría un error.

cadena2 = cadena.upper() #Esto es un nuevo objeto.

# operador de pertenencia (verdadera o falsa):
booleano = 'g' in cadena

#Crea una cadena donde se ven todos los caracteres invisibles como tabulaciones o saltos, representados por \n o \t
stringDebug = repr(cadena)
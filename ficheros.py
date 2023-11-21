#Modos: 
# r (solo lectura),
# w (solo escritura, crea el fichero si no existe y si existe lo borra),
# a (modo añadir, abre el archivo y añade contenido al final).
# r+ (lectura y escritura), w+ (lectura y escritura pero borrando el fichero), a+ (lectura y escritura modo añadir).
# rb, wb, ab, rb+, wb+, ab+ (como los anteriores pero para binarios)

#Abrir el fichero:
try:
    fileHandle = open("hola.txt", "r") #Esto crea un handle para el fichero. r es modo lectura, por defecto es r.
#Si no existe o no tienes permisos, no lo abrirá y dará una excepción.
except:
    print("No se ha podido abrir el fichero")

#Leer línea a línea:
count = 0
for linea in fileHandle:
    count += 1
    print(linea)
print("número de líneas:", count)

fileHandle.seek(0) #Como el fichero ya ha sido leído, debe colocarse de nuevo el cursor al compienzo.

#También se puede operar sobre .readlines() que lee todo el fichero y devuelve una lista de strings

#Buscar en el fichero la línea que contiene una palabra:
for linea in fileHandle.readlines():
    linea.rstrip() #Limpia la cadena de espacios al final.  
    if "From" in linea:
        print(linea)

fileHandle.seek(0)

#Leer contenido completo:
contenido = fileHandle.read() #A diferencia de readLines(), read() devuelve todo el contenido en un solo string.
print(contenido)
print(len(contenido))

fileHandle.close() #se cierra el archivo.


fileHandle = open("hola.txt", 'a')
texto = "Hola mundo desde python \n"
fileHandle.write(texto)
fileHandle.close()

#También se puede usar un bloque with que permite hacer las operaciones sin tener que llamar explícitamente a close()
with open("nuevo.txt", 'w') as fichero:
    fichero.write("ESte es un nuevo fichero\n")
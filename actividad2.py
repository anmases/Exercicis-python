#debemos instalar antes la bibliotecta pyexcel (pip3 install pyexcel y el módulo para tratar ods pip install pyexcel pyexcel-ods)
import pyexcel

#Aquí se genera el CSV a partir del ods. El ods debe estar en este mismo directorio.
libro = pyexcel.load_book(file_name="Dades.ods")
hoja = libro[0]
hoja.save_as("dades.csv")

#Ahora deberemos abrir el fichero csv:
try:
    file = open("dades.csv", "r", encoding="UTF-8") #hay que definir la codificación con la que se ha guardado, si no da error.
except:
    print("No se ha podido abrir el fichero.")

for linea in file:
    if "Francia" in linea:
        print(linea)

file.close()
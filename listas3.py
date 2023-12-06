# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
notas = []

for i in range(5):
    notas.append(int(input("nota: ")))
#todas las notas:
for i in notas:
    print(i)
#nota media:
print(sum(notas)/5)
#nota mayor:
print(max(notas))
#nota menor:
print(min(notas))
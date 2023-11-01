# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia = int(input("dia: "))
mes = int(input("mes: "))
anyo = int(input("año: "))

if anyo > 0:
    if 1<=mes<=12:
        if mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            if 1 <=dia <= 31:
                print("la fecha es correcta.")
            else:
                print("no es correcta")
        elif mes == 2:
            #comprobamos si es bisiesto:
            if anyo % 4 == 0:
                if anyo % 100 != 0 or anyo % 400 == 0:
                    if 0<=dia<=29:
                            print("es correcta")
                    else:
                        if 0<=dia<=28:
                            print("es correcta") 
                        else:
                            print("no es correcta")
            else:
                if 0<=dia<=28:
                    print("es correcta")
                else:
                    print("no es correcta")
        else:
            if 0<=dia<=30:
                print("Es correcta")
            else:
                print("no es correcta")
            

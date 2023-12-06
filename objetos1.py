#Ejemplo básico de clase:
class Persona:
    #constructor
    def __init__(self, nom, edad):
        self.nom = nom
        self.edad = edad


#Herencia:
class Estudiante(Persona):
    def __init__(self, nom, edad, curs):
        super().__init__(nom, edad)
        self.curs = curs

#Encapsulación. Se declaran privados con __ y se añaden sets y gets:
class Coche:
    def __init__(self, modelo, marca):
        self.__modelo = modelo
        self.__marca = marca
    def setMarca(self):
        return self.__marca
    def getMarca(self, novaMarca):
        self.__marca = novaMarca

#polimorfismo:
class Figura:
    def area(self):
        pass
class Cuadrado(Figura):
    def __init__(self, costat):
        self.costat = costat
    def area(self):
        self.costat**2
class Circulo(Figura):
    def __init__(self, radio) -> None:
        self.radio = radio
    def area(self):
        return 3.1415*self.radio**2

#importaciones:
from libreria import Camion
class CamionPequeño(Camion):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

#Decoradores:
class Ejemplo:
    @staticmethod
    def metodoEstatico():
        print("método estático")

def registro(funcion):
    def envoltura(*args, **kwargs):
        print(f"inicio de la ejecución: {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        print(f"fin de la ejecución: {funcion.__name__}")
        return resultado
    return envoltura

'''
    registrar es el decorador.
    envoltura es la nueva función que envuelve la función original func.
    *args y **kwargs son para asegurar que la función envuelta pueda aceptar cualquier número de argumentos posicionales y de palabra clave.
'''
@registro
def saludar(nombre):
    print(f"Hola {nombre}!")

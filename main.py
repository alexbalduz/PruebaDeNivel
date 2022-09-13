from Vehiculo import *
from Camioneta import Camioneta
from Coche import Coche
from Bicicleta import Bicicleta
from Motocicleta import Motocicleta

def catalogar(lista):
    for vehiculo in lista:
        print(type(vehiculo).__name__, vehiculo.__dict__)

def catalogar1(lista, n_ruedas = 2):
    contador = 0
    for vehiculo in lista:
        if n_ruedas == vehiculo.ruedas:
            print(type(vehiculo).__name__)
            contador += 1
    print(f"Se han encontrado {contador} vehículos con {n_ruedas} ruedas")



if __name__ == '__main__':
    a = Camioneta("marron", 8, 120, 400, 500)
    b = Coche("verde", 4, 120, 800)
    c = Bicicleta("azul", 2, "triciclo")
    d = Coche("rosado", 4, 150, 800)
    e = Motocicleta("azul", 2, "triciclo", 150, 200)

    lista_vehiculos = [a, b, c, d, e]
    catalogar(lista_vehiculos)
    catalogar1(lista_vehiculos)

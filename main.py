class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

def catalogar(lista):
    for vehiculo in lista:
        print(type(vehiculo).__name__, vehiculo.__dict__)

def catalogar1(lista, n_ruedas = None):
    contador = 0
    for vehiculo in lista:
        if n_ruedas == vehiculo.ruedas:
            print(vehiculo)
            contador += 1
    if n_ruedas:
        print(f"Se han encontrado {contador} vehículos con {n_ruedas} ruedas:")

a = Camioneta("marron", 8, 120, 400, 500)
b = Coche("verde", 4, 120, 800)
c = Bicicleta("azul", 2, "triciclo")
d = Coche("rosado", 4, 150, 800)
e = Motocicleta("azul", 2, "triciclo", 150, 200)

lista_vehiculos = [a, b, c, d, e]
catalogar(lista_vehiculos)
catalogar1(lista_vehiculos)

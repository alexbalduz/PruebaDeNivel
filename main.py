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
        print(type(vehiculo), vehiculo.__dict__)

if __name__=="__main__":

    a = Camioneta("marron", 8, 120, 400, 500)
    b = Coche("verde", 4, 120, 800)
    c = Bicicleta("azul", 2, "triciclo")
    d = Coche("rosado", 4, 150, 800)
    e = Motocicleta("azul", 2, "triciclo", 150, 200)

    lista_vehiculos = [a, b, c, d, e]
    catalogar(lista_vehiculos)

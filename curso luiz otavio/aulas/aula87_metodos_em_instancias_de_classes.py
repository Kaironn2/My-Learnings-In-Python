from random import randint


class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está à {randint(40, 80)}KM/H')


fusion = Carro('Fusion')
fusion.acelerar()

veloster = Carro('Fusion')
fusion.acelerar()

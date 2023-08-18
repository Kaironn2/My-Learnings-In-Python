# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Company:
    def __init__(self, company):
        self.company = company
        self.car = None
        self.engine = None

    def set_car(self, name):
        self.car = Car(name)

    def set_engine(self, name):
        self.engine = Engine(name)

    def car_spec(self):
        print(
            f'Fabricante: {self.company}\n'
            f'Carro: {self.car.name}\n'
            f'Motor: {self.engine.name}\n'
        )


class Car:
    def __init__(self, name):
        self.name = name


class Engine:
    def __init__(self, name):
        self.name = name


ford = Company('Ford')
ford.set_engine('Duratec 2.0')
ford.set_car('Focus')
ford.car_spec()

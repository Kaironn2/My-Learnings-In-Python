# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

import os


class Company:
    def __init__(self, company):
        self.company = company
        self.cars = {}

    def add_car(self, car_name, engine_name):
        car = Car(car_name, engine_name)
        self.cars[car_name] = car

    def find_car(self, car_name):
        return self.cars.get(car_name, None)

    def company_cars(self):
        print(f'Fabricante: {self.company}')
        for car_name, car in self.cars.items():
            print(car.name)


class Car:
    def __init__(self, name, engine_name):
        self.name = name
        self.engine = Engine(engine_name)


class Engine:
    def __init__(self, name):
        self.name = name


ford = Company('Ford')
ford.add_car('Focus', 'Duratec 2.0')
ford.add_car('Celta', 'Partial 1.8')


while True:

    print('-' * 20)
    ford.company_cars()
    print('-' * 20)

    user_find_car = input(
        '\nDigite o nome do carro que você deseja ver as especificações: ').capitalize()
    if user_find_car == 'Sair':
        print('Programa encerrado.')
        break
    user_car = ford.find_car(user_find_car)

    os.system('cls')

    if user_car:
        print(f'Especificações do {user_find_car}:')
        print(f'Carro: {user_car.name}')
        print(f'Motor: {user_car.engine.name}')
    else:
        print(f'Carro {user_find_car} não encontrado.')

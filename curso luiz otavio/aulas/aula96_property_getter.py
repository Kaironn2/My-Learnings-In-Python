# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um atributo.
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código


class Car:
    def __init__(self, car_color):
        self.car_color = car_color

    @property
    def color_getter(self):  # método se comportando como atributo
        return self.car_color


carro = Car('Preto')
print(carro.color_getter)

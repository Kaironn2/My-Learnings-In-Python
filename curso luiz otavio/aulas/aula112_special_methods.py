# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Alvo: qualquer pessoa, apenas uma string do seu objeto
    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):  # Alvo: outros devs que querem saber como o objeto foi montado
        class_name = type(self).__name__
        # class_name = self.__class__.__name__
        return f'{class_name}(x={self.x}, y={self.y}) '

    def __add__(self, other):
        novo_x = self.x + other.x   # self vai ser o objeto da esquerda
        novo_y = self.y + other.y   # other vai ser o objeto da direita
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        resultado_self = self.x + self.x   # self vai ser o objeto da esquerda
        resultado_other = other.y + other.y   # other vai ser o objeto da direita
        return resultado_self > resultado_other


if __name__ == '__main__':
    p1 = Ponto(1, 2)    # self.x  = 1  |  self.y  = 2
    p2 = Ponto(3, 4)    # other.x = 3  |  other.y = 4
    soma_p3 = p1 + p2        # self | other
    print(f'Soma: {soma_p3}')
    print(f'P1 é maior que P2?: {p1 > p2}')
    print(f'P2 é maior que P1?: {p2 > p1}')

# print(f'{p1!s}')    # chama repr
# print(f'{p1!r}')    # chama repr
# print(repr(p2))     # chama repr

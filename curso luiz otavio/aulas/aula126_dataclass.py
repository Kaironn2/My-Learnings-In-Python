# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import asdict, astuple, dataclass, field, fields

# @dataclass(init=False) # Dessa forma, temos que definir nosso próprio init
# @dataclass(frozen=True) # Não permite alterar valores após a definição
# @dataclass(repr=False) # dessa forma, temos que definir nosso repr


# @dataclass
# class People:
#     name: str
#     age: int
#     last_name: str | None = None

#     def __post_init__(self):
#         self.full_name = f'{self.name} {self.last_name}'

#     @property
#     def full_name(self):
#         return f'{self.name} {self.last_name}'

#     @full_name.setter
#     def full_name(self, full_name):
#         name, *last_name = full_name.split()
#         self.name = name
#         self.last_name = ' '.join(last_name)

#     def set_last_name(self, last_name):
#         self.last_name = last_name


# if __name__ == '__main__':
# Podemos fazer ordenações dessa forma:
#     lista = [People('A', 'Z'), People('B', 'Y'), People('C', 'X')]
#     ordenadas = sorted(lista, reverse=True, key=lambda p: p.name)
#     print(ordenadas)


@dataclass
class People:
    name: str = field(default='MISSING')
    age: int = field(default=22)
    last_name: str | None = None
    addresse: list[str] = field(default_factory=list)

    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'

    @full_name.setter
    def full_name(self, full_name):
        name, *last_name = full_name.split()
        self.name = name
        self.last_name = ' '.join(last_name)

    def set_last_name(self, last_name):
        self.last_name = last_name


if __name__ == '__main__':
    people1 = People('Jonathas', 22)
    people2 = People('Jonathas', 22)
    print(people1)
    people1.full_name = 'Jonathas Oliveira Carneiro'
    print(people1.full_name)
    print(people1)
    print(people1 == people2)
    print(asdict(people1))
    print(asdict(people1).keys())
    print(asdict(people1).items())
    print(astuple(people1))
    print(fields(people1))

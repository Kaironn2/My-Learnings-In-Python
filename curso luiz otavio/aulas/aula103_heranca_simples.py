# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# MRO - Method Resolution Order, é a ordem execução de métodos e atributos.
# Por exemplo na class Aluno que herda pessoa, como o cpf está definido,
# ele irá executar cpf = 'cpf aluno'. Mas no caso da class Pessoa,
# ele irá procurar o cpf na class Cliente primeiro e não encontrará,
# então ele subirá para a próxima classe que ele herdou, que foi Pessoa
# e executará o cpf = '1234

class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('EITA, nem saí da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = 'cpf aluno'
    ...


cliente1 = Cliente('Luiz', 'Otávio')
cliente1.falar_nome_classe()
alunoa1 = Aluno('Maria', 'Helena')
alunoa1.falar_nome_classe()
print(alunoa1.cpf)
# help(Cliente)

"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, branch: int, account: int, balance: float = 0):
        self.branch = branch
        self.account = account
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount: float) -> float:
        self.balance -= amount
        return self.balance

    def deposit(self, amount: float):
        self.balance += amount
        self.details(f'[DEPÓSITO] R${amount}')

    def details(self, msg='', msg2=''):
        print(f'{msg}\n'
              f'O seu saldo atual é R${self.balance:.2f}'
              f'{msg2}')


class CheckingAccount(Account):
    def __init__(self, branch: int,
                 account: int, balance: int, limit: float = 0):
        super().__init__(branch, account, balance)
        self.limit = limit

    def withdraw(self, amount):
        balance_after_withdraw = self.balance - amount

        if balance_after_withdraw >= 0:
            self.balance -= amount
            self.details(f'[SAQUE DE R${amount:.2f} APROVADO]')
            return self.balance

        withdraw_using_limit = self.limit >= abs(balance_after_withdraw)

        if withdraw_using_limit:
            self.balance -= (amount + 10)
            self.details(
                f'[SAQUE DE R${amount:.2f} APROVADO COM LIMITE ESPECIAL]\n'
                '[SERÁ COBRADA UMA TARIFA ADICIONAL DE R$10,00 PELO SERVIÇO]')
            return self.balance

        self.details('[SAQUE NEGADO, SALDO INSUFICIENTE]',
                     f'\nVocê só possui R${self.limit:.2f} de limite de saque'
                     'adicional.')


class SavingsAccount(Account):
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.details(f'[SAQUE DE R${amount:.2f} APROVADO] ')
            return self.balance
        self.details(
            f'[SAQUE NEGADO -> R${amount:.2f} VALOR ACIMA DO SALDO ATUAL]')


if __name__ == '__main__':
    savings_account1 = SavingsAccount(branch=236, account=8069741, balance=300)
    savings_account1.withdraw(300)
    savings_account1.deposit(150)
    savings_account1.withdraw(151)
    print(f'\n{"#" * 40}\n')
    cheking_account1 = CheckingAccount(
        branch=236, account=89607, balance=100, limit=50)
    cheking_account1.withdraw(150)

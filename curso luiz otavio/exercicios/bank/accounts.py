
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

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.branch!r}, {self.account!r}, {self.balance}'
        return f'{class_name, {attrs}}'


class CheckingAccount(Account):
    def __init__(self, branch: int,
                 account: int, balance: int = 0, limit: float = 0):
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

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = (f'{self.branch!r}, {self.account!r},'
                 f'{self.balance}, {self.limit}')
        return f'{class_name, {attrs}}'


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

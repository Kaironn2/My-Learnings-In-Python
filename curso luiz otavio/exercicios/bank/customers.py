import accounts


class People:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.name!r}, {self.age!r}'
        return f'{class_name, {attrs}}'


class Customer(People):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: accounts.Account | None


if __name__ == '__main__':
    c1 = Customer('Kaironn', 22)
    c1.account = accounts.CheckingAccount(236, 80790)
    print(c1)
    print(c1.account)
    c2 = Customer('Jonathas', 22)
    c2.account = accounts.SavingsAccount(3156, 45067, 100)
    print(c2)
    print(c2.account)

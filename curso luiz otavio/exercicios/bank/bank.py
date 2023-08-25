import accounts
import customers


class Bank:
    def __init__(
        self,
        branch: list[int] | None = None,
        account:  list[accounts.Account] | None = None,
        customer: list[customers.People] | None = None,
    ):
        self.branch = branch or []
        self.account = account or []
        self.customer = customer or []

    def _branch_check(self, account):
        if account.branch in self.branch:
            print('_branch_check: True')
            return True
        print('_branch_check: False')
        return False

    def _account_check(self, account):
        if account in self.account:
            print('_account_check: True')
            return True
        print('_account_check: False')
        return False

    def _customer_check(self, customer):
        if customer in self.customer:
            print('_customer_check: True')
            return True
        print('_customer_check: False')
        return False

    def _customer_account_check(self, customer, account):
        if account is customer.account:
            print('_customer_account_check: True')
            return True
        print('_customer_account_check: False')
        return False

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.branch!r}, {self.account!r}, {self.customer!r}'
        return f'{class_name, {attrs}}'

    def authenticate(self, customer:
                     customers.People, account: accounts.Account):
        return self._branch_check(account) and \
            self._customer_check(customer) and \
            self._account_check(account) and \
            self._customer_account_check(customer, account)


if __name__ == '__main__':
    customer1 = customers.Customer('Kaironn', 22)
    checking_account1 = accounts.CheckingAccount(68, 807920)
    customer1.account = checking_account1
    customer2 = customers.Customer('Jonathas', 22)
    checking_account2 = accounts.CheckingAccount(236, 40720)
    customer2.account = checking_account2

    bradesco = Bank()
    bradesco.customer.extend([customer1, customer2])
    bradesco.account.extend([checking_account1, checking_account2])
    bradesco.branch.extend([68, 236])
    print(bradesco.authenticate(customer1, checking_account1))
    print(bradesco.authenticate(customer2, checking_account2))

    if bradesco.authenticate:
        checking_account1.deposit(100)
        checking_account1.withdraw(100)

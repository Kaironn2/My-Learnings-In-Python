

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 1234


call1 = CallMe('123456789')
retorno = call1('Kaironn')
print(f'Return: {retorno}')

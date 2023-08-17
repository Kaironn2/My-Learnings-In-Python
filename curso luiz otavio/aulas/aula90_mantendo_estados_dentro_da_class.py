import os


class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
            return

        print(f'{self.nome} começou a filmar')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} Não está filmando')
            return

        print(f'{self.nome} está parando de filmar...')
        self.filmando = False


camera1 = Camera('Canon')
camera2 = Camera('Sony')

while True:

    option = input(
        '1 - Filmar\n'
        '2 - Parar de filmar\n'
        'a - Canon\n'
        'b - Sony\n'
        'ex: 1b\n\n'
        'Digite uma opção:'
    )

    os.system('cls')

    match option:

        case '1a':
            camera1.filmar()
        case '2a':
            camera2.filmar()
        case '1b':
            camera1.parar_filmar()
        case '2b':
            camera2.parar_filmar()

import os 

ca_co_hi = {}
contador = 0

def validar_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números. Use o . no lugar na vírgula.')

def redefinir_lados(ok):
    global ca_co_hi
    ca_co_hi = {'cateto_oposto': 'Cateto Oposto', 'cateto_adjacente': 'Cateto Adjacente', 'hipotenusa': 'Hipotenusa'}

def redefinir_contador(valor_contador):
    global contador
    contador = valor_contador

while True:

    redefinir_lados(1)

    while True:

        for chave in ca_co_hi:
            print(chave)
        
        opcao = input('Qual opção você deseja inserir? ')

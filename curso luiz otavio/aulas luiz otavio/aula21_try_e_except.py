# Introdução ao Try/Except
# try -> tentar executar o código
# except -> ocorreu algum erro ao tentar executar

number_str = input('Irei dobrar o número inteiro que você digitar: ')
print()

try:
    number_float = float(number_str)
    print(f'O dobro de {number_float} é {number_float * 2: .2f}')
except:
    print('O caractere digitado não é um número')
  
#if number_str.isdigit():
#   number_int = int(number_str)
#    print(f'O dobro de {number_str} é {number_int * 2}')
#else:
#    print('Apenas números são aceitos!')

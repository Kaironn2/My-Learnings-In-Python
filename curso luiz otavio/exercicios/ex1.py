nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
dia_de_nascimento = int(input('Digite o dia em que você nasceu: '))
mes_de_nascimento = int(input('Digite o seu mês de nascimento(Ex: para julho, 07): '))
ano_de_nascimento = int(input('Digite o ano em que você nasceu: '))
altura = float(input('Digite sua altura em metros:'))
idade = 2023 - ano_de_nascimento
verificar_maior_de_idade = idade >= 18
if verificar_maior_de_idade is True:
    maior_de_idade = 'Sim'
else:
    maior_de_idade = 'Não'

print(f'\nNome: {nome}')
print(f'Sobrenome: {sobrenome}')
print(f'Idade: {idade}')
print(f'Data de nascimento: {dia_de_nascimento}/{mes_de_nascimento}/{ano_de_nascimento}')
print(f'É maior de idade? {maior_de_idade}')
print(f'Altura em metros: {altura}m')

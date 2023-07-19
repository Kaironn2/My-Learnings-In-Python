# Variáveis são usadas para salvar algo na memória
# PEP8: inicie variáveis com letras minúsculas, pode usar números e underline
# O sinal de = é o operador de atribuição, ele é usado para atribuir um valor a um nome (variável).
# Uso: nome_completo = 'Luiz Otávio Miranda'

nome_completo = 'Jonathas Barros de Oliveira Carneiro'
soma_dois_mais_dois = 2 + 2
print(nome_completo, soma_dois_mais_dois)


nome = 'Jonathas'
idade = 17
verificar_maior_de_idade = idade >= 18
if verificar_maior_de_idade is True:
    maior_de_idade = 'Sim'
else:
    maior_de_idade = 'Não'
print('Nome: ', nome, '\nIdade:', idade)
print('É maior de idade?', maior_de_idade)

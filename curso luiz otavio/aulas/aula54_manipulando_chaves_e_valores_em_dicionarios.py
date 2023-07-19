dicionario = {}


chave = 'nome'

dicionario[chave] = 'Jonathas'
dicionario['sobrenome'] = 'Barros'

print(dicionario[chave])

dicionario[chave] = 'Maria'

del dicionario['sobrenome']
print(dicionario)
print(dicionario['nome'])

if dicionario.get('sobrenome') is None:
    print('Não existe')
else:
    print(dicionario['sobrenome'])

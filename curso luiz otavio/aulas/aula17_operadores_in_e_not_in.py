# Operadores in e not in
# Strings em python são iteráveis, ou seja, você consegue navegar por cada elemento das strings
# 0 1 2 3 4 5
# j o n a t h a s
# -6-5-4-3-2-1

# Para navegar pelas strings, faça variável[n], sendo n a posição
# A posição começa do 0

# nome = 'jonathas'
# print(nome[1])   Retornará a segunda letra

# print('e' in nome)  Como a letra "e" não está no nome, será False
# print('a' in nome)  Possui a letra "a" em nome, então True
# print('a' not in nome)  Irá verificar se não está em nome

nome = input('Digite seu nome: ')
search = input('Digite o que você deseja pesquisar: ')

if search in nome:
    print(f'{search} está em {nome}')
else:
    print(f'{search} não está em {nome}')

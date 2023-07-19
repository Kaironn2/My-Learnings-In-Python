# Métodos úteis dos dicionários em Pthon
# Len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave 
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - atualiza um dicionário com outro
# import copy # deep copy (cópia profunda)
# update - atualiza um dicionário com outro


pessoa = {
    'nome': 'Jonathas',
    'sobrenome': 'Barros'
}

pessoa.setdefault('idade', 0)
lista = [['nome', 'kaironn'], ['sobrenome', 'DRK']]
tupla = (('nome', 'kai'), ('sobrenome', 'dark'),('idade', 21) )
pessoa.update(lista)
pessoa.update(tupla)

print(len(pessoa)) # quantas chaves tem
print(pessoa.keys()) # chaves
print(pessoa.items()) # chaves e valor
print(pessoa['idade'])

# Função lambd em Python
# A função lambda é uma função como qualquer outra.
# Porém, são funções anônimas que contém apenas uma linha. 
# Ou seja, tudo deve ser contido dentro de uma única expressão

lista = [
    {'nome': 'Jonathas', 'sobrenome': 'Barros'},
    {'nome': 'Braia', 'sobrenome': 'Vinicius'},
    {'nome': 'Micha', 'sobrenome': 'Jhonson'},
    {'nome': 'Luiz', 'sobrenome': 'Dragneel'},
]


# def ordenar(item):
#     return item['sobrenome']

# lista.sort(key=ordenar)

# for item in lista:
#     print('item')

# ordena em ordem alfabética com base no sobrenome
# o return para ordenar o dicionário. Nesse caso, 
# como é ['sobrenome'], será ordenado pelo sobrenome.


lista.sort(key=lambda item: item['nome'])

for item in lista:
    print(item)


# Funções lambda com mais de 1 parametro

multiplicar = lambda multiplicador: lambda numero: numero * multiplicador

print(multiplicar(5)(2))

# Função lambda com quantidad indefinida de parametros

somar = lambda *numeros: sum(numeros)

print(somar(1, 2, 3))

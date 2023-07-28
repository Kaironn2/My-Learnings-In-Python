# List Comprehension é uma forma rápida parar criar listas
# a partirde iteráveis.

# Devemos digitar à esquerda do for o que queremos incluir na lista
# Também é permitido fazer operações
# e usar a variável do for, como no exemplo: 
lista = [numero * 2 for numero in range(1, 11)]

print(lista)


produtos = [

    {'nome': 'papel', 'preço': 10},
    {'nome': 'agua', 'preço': 15},
    {'nome': 'vaso', 'preço': 20}

]

# Mapeamento de dados em list comprehension
# Mapeamento feito à esquerda do for
# No mapeamento, as duas listas sempre terão a mesma quantidade de iteráveis
# Vamos fazer um exemplo para aumentar o valor de cada produto em 5%
# E vamos mudar as chaves de 'nome' para 'produto' e 'preço' para 'valor'
# Pode ser feito em apenas uma linha ou também do modo a seguir: 
# novos_produtos = [{'produto': produto['nome'], 'valor': produto['preço'] * 1.05} if produto['preço'] >= 15 else {**produto} for produto in produtos]

novos_produtos = [
    {'produto': produto['nome'], 'valor': produto['preço'] * 1.05} 
                  if produto['preço'] >= 15 else {**produto} 
                  for produto in produtos
                  ]

print(*novos_produtos, sep='\n')


# Filtro dados em list comprehension
# o filtro é feito à direita do for

novos_produtos = [
    {'produto': produto['nome'], 'valor': produto['preço'] * 1.05} 
                  if produto['preço'] >= 15 else {**produto} 
                  for produto in produtos
                  if produto['preço'] > 10
                  ]

print(*novos_produtos, sep='\n')


# List comprehension com + 1 de um for

# lista = []
# for x in range(5):
#     for y in range(5):
#         lista.append(x, y)

# O exemplo abaixo usando list comprehension vai ter o mesmo output que o de cima no comentário.

lista = [
    (x, y)
    for x in range(1, 4)    # x
    for y in range(1, 6)    # y
    if x != 2               # Filtrar, quando x = 2, não vou adicionar
]

print(lista)

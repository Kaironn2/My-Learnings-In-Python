# List Comprehension é uma forma rápida parar criar listas
# a partirde iteráveis.

# Devemos digitar à esquerda do for o que queremos incluir na lista
# Também é permitido fazer operações
# e usar a variável do for, como no exemplo: 
lista = [numero * 2 for numero in range(1, 11)]

print(lista)


# Mapeamento de dados em list comprehension

produtos = [

    {'nome': 'papel', 'preço': 10},
    {'nome': 'agua', 'preço': 15},
    {'nome': 'vaso', 'preço': 20}

]

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

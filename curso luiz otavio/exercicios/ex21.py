import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


lista_original = [
    {'produto': produto['nome'], 'preco': produto['preco']} for produto in produtos
    ]



produtos_com_aumento = [
    {'produto': produto['nome'], 'preco': produto['preco'] * 1.10} 
    for produto in produtos
]



produtos_ordem_descrecente = [
    {'produto': produto['nome'], 'preco': produto['preco']} for produto in produtos
    ]
produtos_ordem_descrecente.sort(key=lambda item: item['produto'], reverse=True)



produtos_preco_crescente = [
    {'produto': produto['nome'], 'preco': produto['preco']} for produto in produtos
    ]
produtos_preco_crescente.sort(key=lambda item: item['preco'])


print('Lista original:')
for produto in lista_original:
    print(f"Produto: {produto['produto']}: R${produto['preco']:.2f}")

print('\nLista com preço crescente:')
for produto in produtos_preco_crescente:
    print(f"Produto: {produto['produto']}: R${produto['preco']:.2f}")

print('\nLista em ordem descrecente de nome: ')
for produto in produtos_ordem_descrecente:
    print(f"Produto: {produto['produto']}: R${produto['preco']:.2f}")

print('\nProdutos com 10% de aumento:')
for produto in produtos_com_aumento:
    print(f"Produto: {produto['produto']}: R${produto['preco']:.2f}")

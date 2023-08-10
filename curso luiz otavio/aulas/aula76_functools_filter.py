# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]



# Usando lista comprehension
# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 100
# 


def filtrar_preco(produto):
    return produto['preco'] > 100


# O primeiro parâmetro é uma função, o segundo é o iterável.
novos_produtos = filter(                        
    # lambda produto: produto['preco'] > 100,
    filtrar_preco,
    produtos
)


print_iter(produtos)
print_iter(novos_produtos)

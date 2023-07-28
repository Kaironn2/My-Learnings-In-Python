# isinstance - para saber se o objeto é de determinado tipo
# nos argumentos, passaremos o item que queremos verificar
# e depois o tipo que queremos verificar.
# Caso o item passado seja do tipo passado, ele retornará True
# senão, retornará False.
# No segundo argumento da função, você pode usar mais de um tipo.

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Luiz'}
]

for item in lista:

    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))

    if isinstance(item, (float, int)):
        print(item, item * 2)

    if isinstance(item, str):
        print('É uma string')
    
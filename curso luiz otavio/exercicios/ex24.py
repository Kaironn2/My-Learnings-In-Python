"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

list_a     = [1, 2, 3, 4, 5, 6, 7]
list_b     = [1, 2, 3, 4,]
sum_list = []
count = 0

def verify_short_list(list1, list2):
    len_short_list = list1
    if len_short_list > list2:
        len_short_list = list2
    return len_short_list

len_short_list = verify_short_list(list_a, list_b)

for n1, n2 in zip(list_a, list_b):
    sum = n1 + n2
    sum_list.append(sum)
    count += 1
    if count == len_short_list:
        break

print(sum_list)

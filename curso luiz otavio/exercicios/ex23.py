# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from copy import deepcopy

list_city = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Rio de Janeiro', 'Pernambuco']
list_acronym = ['BA', 'SP', 'MG', 'RJ']
short_list = []
large_list = []
combined_list = []
count = 0

def verify_short_list(list1, list2):
    global short_list, large_list
    if len(list1) > len(list2):
        short_list = deepcopy(list2)
        large_list = deepcopy(list1)
    else:
        short_list = deepcopy(list1)
        large_list = deepcopy(list2)

verify_short_list(list_city, list_acronym)

if len(short_list[0]) == 2:
    for city, acronym in zip(large_list, short_list):
        current_list = [city, acronym]
        combined_list.append(current_list)
        count += 1
        if count == len(short_list):
            break

else:
    for city, acronym in zip(short_list, large_list):
        current_list = [city, acronym]
        combined_list.append(current_list)
        count += 1
        if count == len(short_list):
            break


for city, acronym in combined_list:
    print(f'{city}, {acronym}')

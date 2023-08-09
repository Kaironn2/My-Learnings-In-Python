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

lista_cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Rio de Janeiro', 'Pernambuco']
lista_siglas = ['BA', 'SP', 'MG', 'RJ']
menor_lista = []
maior_lista = []
lista_combinada = []
contador = 0

def verify_small_list(lista1, lista2):
    global menor_lista, maior_lista
    if len(lista1) > len(lista2):
        menor_lista = deepcopy(lista2)
        maior_lista = deepcopy(lista1)
    else:
        menor_lista = deepcopy(lista1)
        maior_lista = deepcopy(lista2)

verify_small_list(lista_cidades, lista_siglas)

if len(menor_lista[0]) == 2:
    for cidade, sigla in zip(maior_lista, menor_lista):
        lista_atual = [cidade, sigla]
        lista_combinada.append(lista_atual)
        contador += 1
        if contador == len(menor_lista):
            break

else:
    for cidade, sigla in zip(menor_lista, maior_lista):
        lista_atual = [cidade, sigla]
        lista_combinada.append(lista_atual)
        contador += 1
        if contador == len(menor_lista):
            break


for cidade, sigla in lista_combinada:
    print(f'{cidade}, {sigla}')

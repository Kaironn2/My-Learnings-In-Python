# Concatenar lista
# Estender lista

lista_a = [1, 2 , 3]
lista_b = [4, 5 , 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) # o método é aplicado direto na lista A, alterando ela.
print(lista_a, lista_c)

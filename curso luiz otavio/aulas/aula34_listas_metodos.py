# Listas em python
# Tipo list - mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - indíces e fatiamento
# Métodos úteis: append, insert, pop, del, clear, extend, +
# Uma lista vazia é False
# CRUD -> Creat, read, update, delete
# Quando mexer numa lista, preferencialmente mexer nos ultimos itens para exigir menos processamento
# append() -> adiciona item no final da lista
# pop() -> remove ultimo item da lista
# del() -> deleta um item de indice escolhido


string ='ABCDE'     # 5 caracteres (len)
lista = [123, True, 'Jonathas Barros', 1.2, []]
lista.append('Kaironn')
print(lista)
ultimo_valor = lista.pop() # O método pop retorna o ultimo valor
print(lista, 'Removido', ultimo_valor)

# Desempacotamento em chamadas
# Métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    ['Maria', 'Helena',],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda']
]

p, b, *_, u = lista  # O *_ significa resto, então se eu quiser ignorar e pegar itens especificos do inicio ou final
print(p, u)          # basta usar *_ pra preencher os que não me servem

print('\n\n\n')


print(salas)


print('\n\n\n')


print(*salas)

print('\n\n\n')


print(*salas, sep='\n')

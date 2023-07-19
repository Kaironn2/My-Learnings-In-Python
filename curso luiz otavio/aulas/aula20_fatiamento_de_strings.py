# Fatiamento de Strings
# 012345678
# Olá mundo
# -987654321
# Fatiamento [i:f:p] [::] -> i = onde inicia, f = onde acaba, p = de quantas em quantas vai pular
# Se o p = -1, a string será invertida
# Obs.: a função len retorna a quantidade de caracteres da str

variavel = 'Olá mundo'
print(len(variavel))
print(variavel[0:9:2])
print(variavel[::-1]) # String invertida 

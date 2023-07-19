# Iterando string com while

nome = 'Jonathas Barros' # Strings são iteráveis
nome_novo = ''

tamanho_nome = len(nome)
contador = 0

while contador != tamanho_nome:
    
    letra = nome[contador]
    nome_novo += f'*{letra}'

    contador += 1

nome_novo += '*'

print(nome_novo)
    
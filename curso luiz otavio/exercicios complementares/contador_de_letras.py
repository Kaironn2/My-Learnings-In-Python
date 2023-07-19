frase = 'O Python é uma linguagem de programação ' \
'multiparadigma.' \
'Python foi criado por Guido van Rossum'.lower()

i = 0
letra_mais_repetida = ''
letra_mais_repetida_qntd = 0

while i < len(frase):
    letra_atual = frase[i]
    letra_atual_repeticao = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if letra_atual_repeticao > letra_mais_repetida_qntd:
        letra_mais_repetida = letra_atual
        letra_mais_repetida_qntd = letra_atual_repeticao

    print(letra_atual, letra_atual_repeticao)

    i += 1

print(f'A letra mais repetida foi a letra {letra_mais_repetida.upper()},', end=' ')
print(f'repetindo-se por {letra_mais_repetida_qntd} vezes')

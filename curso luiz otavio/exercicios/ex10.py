frase = 'O Python é uma linguagem de programação ' \
'multiparadigma.' \
'Python foi criado por Guido van Rossum'.lower()

i = 0
while i < len(frase):
    letra_atual = frase[i]
    qnts_vezes_letra_repete = frase.count(letra_atual)
    letra_mais_repetida = ''
    letra_mais_repetida_qnt = 0
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if qnts_vezes_letra_repete > letra_mais_repetida_qnt:
        letra_mais_repetida_qnt = qnts_vezes_letra_repete

    print(letra_atual, qnts_vezes_letra_repete)
    i += 1

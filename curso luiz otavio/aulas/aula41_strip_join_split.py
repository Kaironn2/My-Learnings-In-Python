# split e join com list e str
# split divide uma string
# join une uma string

frase = '        Eu jogo de rengar   ,      mas só no top       '
palavras_da_frase_raw = frase.split(',')

lista_frases = []
for i, frase in enumerate(palavras_da_frase_raw):
    lista_frases.append(palavras_da_frase_raw[i].strip())

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)


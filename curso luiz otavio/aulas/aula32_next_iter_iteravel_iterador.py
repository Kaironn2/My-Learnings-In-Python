# iterável -> str, range, etc (__iter__)
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o próximo valor
# Iter -> me entregue seu iterador


texto = 'Jonathas'
iterador = iter(texto)

# Por baixo dos panos, o for funciona assim:

#while True:
#    try:
#        letra = next(iterador)
#        print(letra)
#    except StopIteration:
#        break

for letra in texto:
    print(letra)

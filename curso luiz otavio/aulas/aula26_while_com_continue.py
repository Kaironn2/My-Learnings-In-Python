# O continue serve para voltar para o início do laço

contador = 0

while contador < 30:
    contador += 1

    if contador == 2:
        print(f'Não irei mostrar o número {contador}')
        continue

    if contador >= 5 and contador <= 10:
        print(f'Não vou mostrar o número {contador}')
        continue
    
    print(contador)

    if contador == 25:
        break

print('FIM')

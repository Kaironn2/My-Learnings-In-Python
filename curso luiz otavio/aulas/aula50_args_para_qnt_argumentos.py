# args - argumentos não nomeados
# * - *args (empacotamento e desempacotamento)

somatoria = 0

x, y, *resto = 1, 2, 3, 4
#print(resto)


def soma(*args):
    somatoria = 0
    contador = 0

    #args = list(args)          # você pode converter as tuplas dos *args para list


    for numero in args:
        contador += 1

        if len(args) == contador:
            print(f'{numero}', end=' = ')
        else:
            print(f'{numero}', end=' + ')
        
        somatoria += numero

    print(somatoria)

soma(1, 2, 3, 4, 5, 6)

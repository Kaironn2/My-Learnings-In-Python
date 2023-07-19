tabuada = 1

while True:
    
    valor = int(input('Digite o valor que você quer ver a tabuada: '))

    while tabuada <= 10:
        resultado = valor * tabuada
        print(f'{valor} x {tabuada} = {resultado}')
        tabuada += 1
    tabuada = 1

    sair = input('\nVocê deseja sair do program? [s]im: ').lower().startswith('s')

    if sair:
        break
    
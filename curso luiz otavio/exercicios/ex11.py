palavra_secreta = 'jett'
letras_encontradas = 0
letras_encontradas_round_atual = 0
letras_erradas = ''
caractere_digitado = ' '
tentativas = 0
pontos = 0
l1 = '_'
l2 = '_'
l3 = '_'
l4 = '_'

print(
    'Vamos jogar o jogo da palavra secreta. '
    'Eu irei pensar em uma palavra, e você terá que adivinhar.\n'
    'Você irá falar letra por letra, e eu lhe responderei se', end=' '
    'tem essa letra na palavra e o total de letras restantes.\n'
    'obs: no caso de mais de uma letra digitada, apenas a primeira irá contar.'
    '\nDICA: VALORANT\n'
)

print(f'\n{l1} {l2} {l3} {l4}\n')

while tentativas < 10:

    print(f'\n---------------------------TENTATIVA {tentativas + 1}---------------------------'
              f'\ntentativas restantes: {10 - tentativas}')
    print(f'\n{l1} {l2} {l3} {l4}\n')
    print(f'Letras usadas que não estão na palavra: {letras_erradas}\n')
    
    while True:
        caractere_digitado = input('\nDigite uma letra: ').upper()

        if len(caractere_digitado) < 1:
            continue

        if caractere_digitado in 'ABDCEFGHIJKLMNOPQRSTUVWXYZ':
            break
        else:
            print('Apenas letras são aceitas, por favor, tente novamente.\n')

    print()

    letra = caractere_digitado[0]
    
    if letra in palavra_secreta:
        for i in palavra_secreta:
            if i == letra:
                letras_encontradas += 1
                letras_encontradas_round_atual += 1
                pontos += 10
            
        if palavra_secreta[0] == letra:                #achar uma forma de automatizar a substituição
            l1 = letra                                 #dos espaços da palavra secreta pelas letras
        if palavra_secreta[1] == letra:                #em suas devidas posições
            l2 = letra
        if palavra_secreta[2] == letra:
            l3 = letra
        if palavra_secreta[3] == letra:
            l4 = letra
            
        if letras_encontradas_round_atual == 1:
            print(f'A letra {letra} apareceu {letras_encontradas_round_atual} vez.')
        else:
            print(f'A letra {letra} apareceu {letras_encontradas_round_atual} vezes.')
    else:
        if letra in letras_erradas:
            print('Essa letra já foi escolhida, tente outra.')
            continue
        
        print(f'Na palavra secreta não possui a letra {letra}.')
        letras_erradas += letra
        pontos -= 5
    
    if letras_encontradas == len(palavra_secreta):
        break

    tentativas += 1
    caractere_digitado = ' '
    letras_encontradas_round_atual = 0    

if tentativas == 10:
        print(f'Que pena! Suas tentativas acabaram. a palavra secreta era {palavra_secreta}.')
else:
    print(f'\nParabéns!!! Você acertou com {tentativas} tentativas, fazendo um total de {pontos} pontos!')

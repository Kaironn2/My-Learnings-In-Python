from random import randint
from time import sleep
import os

palavra_secreta = ['RENGAR', 'FADE', 'SAADHAK', 'SASUKE', 'FRAJOLA', 'CRUNCHYROLL', 'GOIABA', 'RAIDEN', 'STRANGER THINGS', 
                   'DARK STORM SLAYER', 'CAMMY']
dica_palavra_secreta = ['Campeão do lol', 'Agente do Valorant', 'Proplayer de Valorant', 'Personagem de Naruto',
                        'Personagem de Looney Tunes', 'Serviço de Streaming', 'FRUTA', 
                        'Personagem de Mortal Kombat', 'Série da Netflix', 'Melhor Jogador de Rengar', 'Personagem de Street Fighter']

letras_acertadas = ''
letras_usadas = ''
pontos = 0
tentativas = 15
validar_reset = 0
randomizer = 0
quantidade_de_palavras = len(palavra_secreta) - 1
nao_repetir = []
finalizador = 0
pontos_totais = 0
limite = quantidade_de_palavras + 1
palavra_secreta_validar = ''
dica_palavra_secreta_atual = ''

while True:

    if finalizador == limite:
        break

    if validar_reset == 0:
        while True:
            
            randomizer = randint(0, quantidade_de_palavras)

            if randomizer not in nao_repetir:
                nao_repetir.append(randomizer)
                palavra_secreta_atual = palavra_secreta[randomizer]
                dica_palavra_secreta_atual = dica_palavra_secreta[randomizer]
                validar_reset == 1
                break

    
    validar_reset = 1

    
    print(f'Letras usadas: {letras_usadas}\n')

    print(f'--------TENTATIVA(S) {tentativas}--------\n')
    print(f'DICA: {dica_palavra_secreta_atual}')
    letra_digitada = input('Digite uma letra: ').upper()


    if letra_digitada == '':
        os.system('cls')
        continue


    if letra_digitada in letras_usadas:
        os.system('cls')
        print('Você já digitou essa letra! Tente outra, por favor.')
        continue


    if len(letra_digitada) != 1:
        os.system('cls')
        print('Por favor, digite apenas uma letra.')
        continue


    if letra_digitada not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        os.system('cls')
        print('Apenas letras são aceitas.')
        continue


    if letra_digitada in palavra_secreta_atual:
        letras_acertadas += letra_digitada

    
    if letra_digitada not in letras_usadas:
        letras_usadas += letra_digitada

    palavra_formada = ''
    for letra in palavra_secreta_atual:

        if letra in letras_acertadas:
            palavra_formada += letra

        elif letra == ' ':
            palavra_formada += ' '
        
        elif letra == '-':
            palavra_formada += '-'
        
        else:
            palavra_formada += '_'

    os.system('cls')
    print(palavra_formada)

    tentativas -= 1

    
    if palavra_formada == palavra_secreta_atual:
        print('Parabéns, você adivinhou a palavra secreta.')

    elif tentativas == 0:
        print('Que pena, suas tentativas acabaram :(')

    else:
        continue
    
    finalizador += 1

    reset = input('Você deseja jogar novamente? [s]im [n]ão: ').lower().startswith('n')


    if reset:
        break

    else:
        print('Reiniciando o jogo...')
        tentativas = 12
        letras_usadas = ''
        letras_acertadas = ''
        validar_reset = 0
        os.system('cls')


print('.'), sleep(0.5), print('.'), sleep(0.5), print('.'), sleep(0.5)
print('Jogo encerrado'), sleep(2)

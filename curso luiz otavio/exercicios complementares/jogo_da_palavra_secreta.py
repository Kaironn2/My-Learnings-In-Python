from random import randint
import os

palavra_secreta = ['RENGAR', 'FADE', 'SAADHAK', 'SASUKE', 'FRAJOLA', 'CRUNCHYROLL', 'GOIABA', 'RAIDEN']
dica_palavra_secreta = ['Campeão do lol', 'Agente do Valorant', 'Proplayer de Valorant', 'Personagem de Naruto',
                        'Personagem de Looney Tunes', 'Serviço de Streaming', 'FRUTA', 
                        'Personagem de Mortal Kombat']
letras_acertadas = ''
letras_usadas = ''
pontos = 0
tentativas = 10
validar_reset = 0
randomizer = 0
quantidade_de_palavras = len(palavra_secreta) - 1
nao_repetir = []
finalizador = 0
pontos_totais = 0

while True:

    print(f'\nLetras usadas: {letras_usadas}\n')

    if validar_reset == 0:                          #chave para resetar e mudar a palavra e dica
        while True:
            randomizer = randint(0, quantidade_de_palavras)
            
            if randomizer not in nao_repetir:
                nao_repetir.append(randomizer)
                break

        palavra = palavra_secreta[randomizer]
        dica = dica_palavra_secreta[randomizer]
        validar_reset += 1

    print(f'--------TENTATIVA(S) {tentativas}--------\n')
    print(f'DICA: {dica}')
    letra_digitada = input('Digite uma letra: ').upper()

    if len(letra_digitada) != 1:
        os.system('cls')
        print('Digite apenas uma letra.\n')
        continue
    
    if letra_digitada not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        os.system('cls')
        print('Apenas letras são aceitas, tente novamente\n')
        continue

    if letra_digitada in palavra:                       #valida e adiciona a letra digitada 
        letras_acertadas += letra_digitada              #em letras acertadas
    
    palavra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:           #verifica e adiciona a letra digitada   
            palavra_formada += letra_secreta            #no lugar dos caracteres _
            pontos += 10
        else:
            palavra_formada += '_'                      
            pontos -= 5

            if letra_digitada not in letras_usadas:
                letras_usadas += letra_digitada         #verificação para impedir de repetir a adição
                                                        #das mesmas letras nas letras usadas
    os.system('cls')
    print(palavra_formada, '\n')
    tentativas -= 1

    if palavra_formada == palavra:
        print('Parabéns! Você conseguiu concluir o desafio da palavra secreta\n'
        f'Você fez um total de {pontos} pontos, com {tentativas} tentativas restantes.')
        finalizador += 1
    elif tentativas == 0:
        print('Que pena! Suas tentativas acabaram.')
    else:
        continue
    
    pontos_totais += pontos
    if finalizador > len(nao_repetir):
        break

    reset = input('Você deseja jogar novamente? [s]im [n]ão: ').lower().startswith('s')

    if reset:
        print('Reiniciando o jogo...')
        tentativas = 10
        letras_usadas = ''
        letras_acertadas = ''
        pontos = 0
        validar_reset = 0
        os.system('cls')
    else:
        break

print(
f'Você fez um total de {pontos_totais} pontos!'
'Jogo finalizado!'
)

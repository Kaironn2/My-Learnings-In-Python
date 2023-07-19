import os
from time import sleep

count_alternativas = 0
count_questao_atual = 1
respostas_usuario = []
questoes_acertadas = 0
questoes_erradas = 0

questoes = [
    {   
        'pergunta': 'Quanto é 2 + 2?',
        'alternativas': ['A', 'B', 'C', 'D'],
        'valor_alternativas': ['1', '3', '4', '5'],
        'resposta': '4',
        'resposta_alternativa': 'C'
    },

    {
        'pergunta': 'Quanto é 5 * 5?',
        'alternativas': ['A', 'B', 'C', 'D'],
        'valor_alternativas': ['25', '55', '10', '51'],
        'resposta': '25',
        'resposta_alternativa': 'A'
    },

    {
        'pergunta': 'Quanto é 10 / 2?',
        'alternativas': ['A', 'B', 'C', 'D'],
        'valor_alternativas': ['4', '5', '2', '1'],
        'resposta': '5',
        'resposta_alternativa': 'B'
    },
    
    {
        'pergunta': 'Quanto é 2³?',
        'alternativas': ['A', 'B', 'C', 'D'],
        'valor_alternativas': ['16', '6', '4', '8'],
        'resposta': '8',
        'resposta_alternativa': 'D'
    }

]

for pergunta in questoes:

    pergunta_atual = pergunta['pergunta']
    alternativas_atuais = pergunta['alternativas']
    qnt_alternativa_atual = len(pergunta['alternativas']) - 1
    count = 0

    os.system('cls')
    
    while True:


        print(f'QUESTÃO {count_questao_atual}: {pergunta_atual}')


        while True:                                                                         # Mostra as alternativas
            alternativa_atual = pergunta['alternativas'][count_alternativas]
            valor_alternativa_atual = pergunta['valor_alternativas'][count_alternativas]
            print(f'{alternativa_atual}) {valor_alternativa_atual}')

            if count_alternativas == qnt_alternativa_atual:
                count_alternativas = 0
                break
            
            count_alternativas += 1


        resposta_alternativa_usuario = input('\nDigite a alternativa escolhida: ').upper()


        if resposta_alternativa_usuario in alternativas_atuais:
            break
        
        os.system('cls')
        print('Por favor, digite uma alternativa válida.')


    verificador_alternativa = 0

    for alternativa in pergunta['alternativas']:
        if alternativa == resposta_alternativa_usuario:
            verificador_alternativa = count
        count += 1


    valor_resposta_usuario = pergunta['valor_alternativas'][verificador_alternativa]


    if valor_resposta_usuario == pergunta['resposta']:
        acerto_erro_usuario = 'Certo'
        questoes_acertadas += 1
    else:
        acerto_erro_usuario = 'Errado'
        questoes_erradas += 1

    lista_resposta_usuario_atual = []
    lista_resposta_usuario_atual.append(resposta_alternativa_usuario)
    lista_resposta_usuario_atual.append(valor_resposta_usuario)
    lista_resposta_usuario_atual.append(acerto_erro_usuario)

    respostas_usuario.append(lista_resposta_usuario_atual)
    count_questao_atual += 1

os.system('cls')

rendimento_prova = 100 * questoes_acertadas / (questoes_acertadas + questoes_erradas)
quant_perguntas = len(questoes)

if questoes_erradas == 0:
    print(f'Você acertou todas as {quant_perguntas} questões!')

elif questoes_acertadas == 0:
    print(f'Você errou todas as {quant_perguntas} questões :(')

else:
    print(f'Você acertou {questoes_acertadas} questões e errou {questoes_erradas} tendo um proveito de {rendimento_prova}%')


ver_gabarito = input('Você deseja ver o gabarito? [s]im [n]ão: ').upper().startswith('S')
os.system('cls')

if ver_gabarito:
    count = 0

    for resposta in questoes:
        resposta_atual = resposta['resposta_alternativa']
        print(
            
            f'QUESTÃO {count + 1}:\n '
            f'Você escolheu a alternativa {respostas_usuario[count][0]}\n'
            f'A resposta é {resposta_atual}\n'
        )
        count += 1

print('PROGRAMA FINALIZADO!')

import os

user_responses = []
letters = ['A', 'B', 'C', 'D']
count = 0

questions = [
    {   
        'question': 'QUESTÃO 1: Quanto é 2 + 2?',
        'options': ['1', '3', '4', '5'],
        'response': '4'
    },

    {
        'question': 'QUESTÃO 2: Quanto é 5 * 5?',
        'options': ['25', '55', '10', '51'],
        'response': '25'
    },

    {
        'question': 'QUESTÃO 3: Quanto é 10 / 2?',
        'options': ['4', '5', '2', '1'],
        'response': '5'
    }

]

for question in questions:

    while True:

        alternative_a = question['options'][0]
        alternative_b = question['options'][1]
        alternative_c = question['options'][2]
        alternative_d = question['options'][3]

        print(
            question['question'],
            '\nA)', question['options'][0],
            '\nB)', question['options'][1],
            '\nC)', question['options'][2],
            '\nD)', question['options'][3]
          )
        response_user = input('Digite a alternativa escolhida: ').upper()

        if response_user[0] in 'ABCD':
            break

        os.system('cls')
        print('Por favor, digite uma alternativa válida [ABCD]')

    if response_user[0] == 'A':
        if alternative_a == question['response']:
            response_confirmation = 'Certo'
            print('CERTO')
        else:
            response_confirmation = 'Errado'
            print('ERRADO')
    elif response_user[0] == 'B':
        if alternative_b == question['response']:
            response_confirmation = 'Certo'
            print('CERTO')
        else:
            response_confirmation = 'Errado'
            print('ERRADO')
    elif response_user[0] == 'C':
        if alternative_c == question['response']:
            response_confirmation = 'Certo'
            print('CERTO')
        else:
            response_confirmation = 'Errado'
            print('ERRADO')
    elif response_user[0] == 'D':
        if alternative_d == question['response']:
            response_confirmation = 'Certo'
            print('CERTO')
        else:
            response_confirmation = 'Errado'
            print('ERRADO')

    user_current_response = [letters[count], response_confirmation]
    user_responses.append(user_current_response)
    count += 1

    os.system('cls')

count = 0

for resposta in user_responses:
    count += 1
    print(f'Questão {count} - {resposta[1]}')

print(
    'A seguir, o horário que você está lendo essa mensagem.'
    'formato aceito: 23:47'
)
horario = input('Digite o horário: ')

hora = horario[0] + horario[1]
hora_int = int(hora)
minutos = horario[3] + horario[4]
minutos_int = int(minutos)

if hora_int > 23 or minutos_int > 59:
    print('Desculpe, o horário digitado não é válido.')
else: 
    if 11 >= hora_int >= 0:
        print(f'Bom dia!! Agora são exatamente {horario}')

    elif 17 >= hora_int > 11:
        print(f'Boa tarde!! Agora são exatamente {horario}')

    elif 23 >= hora_int >= 18:
        print(f'Boa noite!! Agora são exatamente {horario}')

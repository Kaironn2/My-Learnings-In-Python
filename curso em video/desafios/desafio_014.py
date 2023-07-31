import os

def celsius_to_kelvin(temperatura):
    temperatura_em_kelvin = temperatura + 273
    return temperatura_em_kelvin

def kelvin_to_celsius(temperatura):
    temperatura_em_celsius = temperatura - 273
    return temperatura_em_celsius

def celsius_to_farenheit(temperatura):
    temperatura_em_farenheit = (temperatura * 1.8) + 32
    return temperatura_em_farenheit

def farenheit_to_celsius(temperatura):
    temperatura_em_celsius = (temperatura - 32) / 1.8
    return temperatura_em_celsius

def temperatura_user(temperatura):
    
    while True:
        
        try:
            temperatura = float(input('Digite a temperatura que você quer converter: '))
            os.system('cls')
            return temperatura
        except ValueError:
            print('Valor inválido. Por favor, digite apenas número. No caso de decimais, use . invés de vírgula.')
            os.system('cls')
            continue

def validate_option(mensagem):
    global encerrar

    while True:

        opcao_user = input(f'{mensagem}').upper()

        if opcao_user == '':
            os.system('cls')
            continue
        elif opcao_user[0] not in 'SN':
            os.system('cls')
            print('Opção inválida. Por favor, digite SIM para continuar e NÃO para finalizar.')
            continue
        else:
            if opcao_user == 'S':
                encerrar = False
            else:
                encerrar = True
            break


def opcoes_temperatura(opcao):
    
    print(
        'De qual escala é a temperatura que você quer converter?\n'
        '1 - Kelvin\n'
        '2 - Celsius\n'
        '3 - Farenheit\n'
        )

    while True:
        opcao_user = input(f'Digite a opção desejada: ')
        
        if opcao_user[0] in '123':
            os.system('cls')
            return opcao_user
        
        os.system('cls')
        print('Opção inválida. Por favor, digite uma das opções listadas.')
        


while True:
    
    opcao = opcoes_temperatura('x')
    
    temperatura = temperatura_user('y')
    
    match opcao:
        
        case '1':
            temperatura_em_celsius = kelvin_to_celsius(temperatura)
            temperatura_em_kelvin = temperatura
            temperatura_em_farenheit = celsius_to_farenheit(temperatura_em_celsius)
            
        case '2':
            temperatura_em_celsius = temperatura
            temperatura_em_kelvin = celsius_to_kelvin(temperatura_em_celsius)
            temperatura_em_farenheit = celsius_to_farenheit(temperatura_em_celsius)
        
        case '3':
            temperatura_em_celsius = farenheit_to_celsius(temperatura)
            temperatura_em_kelvin = celsius_to_kelvin(temperatura_em_celsius)
            temperatura_em_farenheit = celsius_to_farenheit(temperatura_em_celsius)

    
    print(f'Temperatura em celsius: {temperatura_em_celsius:.1f}°C\n'
          f'Temperatura em Kelvin: {temperatura_em_kelvin:.1f}K\n'
          f'Temperatura em Farenheit: {temperatura_em_farenheit:.1f}°F\n')
    
    validate_option('Você deseja converter outra temperatura? [s]im [n]ão: ')

    if encerrar:
        print('Programa encerrado.')
        break

    os.system('cls')

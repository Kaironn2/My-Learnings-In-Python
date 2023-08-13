import os

def name_analy(name):
    splited_name = name.split()
    first_name = splited_name[0]
    full_name = ''
    full_name_lenght = 0
    for word in splited_name:
        full_name += word + ' '
        full_name_lenght += len(word)
    print(
        f'Seu primeiro nome é {first_name} e tem {len(first_name)} letras.\n'
        f'E seu nome completo é {full_name} e tem {full_name_lenght} letras.'
          )

def name_verify():

    name = input('Digite o seu nome: ').upper().lstrip(' ')

    switch_name_analy = True
    for letter in name:
        if letter not in 'ABCDEFGHIJKLMNOPQRSTUVWYXZ ':
            switch_name_analy = False
    
    if switch_name_analy:
        name_analy(name)
    else:
        print('Por favor, não digite números ou caracteres especiais.')


name_verify()

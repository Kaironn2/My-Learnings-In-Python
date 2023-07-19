name = input('Digite seu nome: ')
age = input('Digite sua idade: ')
print()
if name and age:
    age_int = int(age)
    print(f'Seu nome é {name}')
    print(f'Sua idade é {age_int}')
    print(f'Seu nome invertido é {name[::-1]}')
    if ' ' in name:
        print('Seu nome tem espaços')
    else:
        print('Seu nome não tem espaços')
    print(f'Seu nome tem {len(name)} letras')
    print(f'A última letra do seu nome é {name[-1]}')
else:
    print('Desculpe, você deixou um dos campos vazios.')

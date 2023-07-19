nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura**2)

print(f'Seu nome é {nome}, tem {altura:.2f}m de altura, pesa {peso:.2f}kg', end=' ')
print(f'e seu indíce de massa corpórea é: {imc:.2}')
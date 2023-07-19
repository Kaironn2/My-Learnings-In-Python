# Operadores lógicos 
# and (e) or (ou) not(não)

# and - Todas as condições precisam ser verdadeiras, 
# senão, a expressão será considerada completamente falsa.
# Ex: print(True and False and True) retornará False
# EX: print(True and True and True) retornará True

user_digitado = input('Digite o seu usuário: ')
senha_digitada = input('Digite sua senha: ')

user_permitido = 'Kaironn'
senha_permitida = 'Win@'

if user_digitado == user_permitido and senha_digitada == senha_permitida:
    print('\nVocê conectou-se ao seu usuário com sucesso!')
else:
    print('\nDesculpe, mas alguma das credenciais digitadas está errada.')

# Formatação básica de strings
# s - string
# d - int
# f - float
# .<número de dígitos>f
# x ou X - Hexadecimal
# (Caractere)(><^)(quantidade)
# Força o número a aparecer antes dos zeros
# > - esquerda
# < - direita
# ^ - centro
# Sinal - + ou -  
# Ex.: 0 > 100,.1f
# Conversion Flags - !r !s !a

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{10000.981541654: .2f}')
print(f'O hexadecimal de 1500 é {1500:08X}')

# Imprecisão de Números Flutuantes

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 3)) # Arredonda a ultima casa decimal, e corta os zeros.

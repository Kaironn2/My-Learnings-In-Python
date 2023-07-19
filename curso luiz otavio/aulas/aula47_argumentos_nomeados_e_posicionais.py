# Parâmetro é a variável na função
# Argumento é o valor definido pro parâmetro
# Posso definir um valor padrão pro parâmetro para caso ele não receba outro valor
# 0 é um valor false



def soma (x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=} | x + y + z = ', x + y + z)
    else:
        print(f'{x=} {y=} | x + y  = ', x + y)

soma(1, 2, 3)
soma(y=2, x=1, z=3) # se mudar a ordem, mas nomear os argumentos, poderá manter a ordem.
soma(1, y=2, z=3) # A partir do argumento nomeados, todos que vierem depois tem que ser nomeados
soma(1, 2)

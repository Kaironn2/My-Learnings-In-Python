# Retorno de Valores das funções (return)
# Por padrão, funções retornam None, então tenho que definir um return dentro da função

def soma(x, y):
    if y == 9:
        return 10, 20   # Se essa condição for verdadeira, nada abaixo será executado
    print(y)
    return x + y        # o código para no return
    print(x)            # códigos abaixo do return nunca serão executados



soma1 = soma(1, 3)
soma2 = soma(2, 3)
soma3 = soma1 + soma2
print(f'{soma1=}, {soma2=}, {soma3=}')

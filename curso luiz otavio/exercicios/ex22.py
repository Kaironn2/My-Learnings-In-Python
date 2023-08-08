def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def criar_funcao(funcao, x):    # Primeiro parametro é a função, o segundo o x, e o terceiro é o y
    def closure(y):
        return funcao(x, y)
    return closure


soma = criar_funcao(somar, 5)
subtracao = criar_funcao(subtrair, 10)          # aqui atribuímos o primeiro e o segundo parâmetro
multiplicacao = criar_funcao(multiplicar, 10)   # sendo eles a função e o x, respectivamente

print(subtracao(5))                             # depois chamamos a variável que guardamos os dois parâmetros
print(soma(10), multiplicacao(10))              # e atribuímos o y, para poder fechar a função.

def somar(x, y):
    return x + y

def multiplicar(x, y):
    return x * y

def criar_funcao(funcao, x):
    def closure(y):
        return funcao(x, y)
    return closure


soma = criar_funcao(somar, 5)
multiplicacao = criar_funcao(multiplicar, 10)

print(soma(10), multiplicacao(10))

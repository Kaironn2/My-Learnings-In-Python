def funcao_multiplicar(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = funcao_multiplicar(2)
triplicar = funcao_multiplicar(3)
quadruplicar = funcao_multiplicar(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

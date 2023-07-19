# Closure e funções que retornam outras funções

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar
    

bom_dia = criar_saudacao('Bom dia')
boa_noite = criar_saudacao('Boa noite')

print(bom_dia('Luiz'))
print(boa_noite('Luiz'))

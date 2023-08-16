# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):    # Passamos lista=None como parâmetro
    if lista is None:   # Aqui verificamos se a lista é None, para saber se criamos uma nova                  
        lista = []
    lista.append(nome)
    return lista        


cliente1 = adiciona_clientes('luiz')    # Quando o parametro não for passado, lista=None será True, criando uma lista nova
adiciona_clientes('Joana', cliente1)    
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)

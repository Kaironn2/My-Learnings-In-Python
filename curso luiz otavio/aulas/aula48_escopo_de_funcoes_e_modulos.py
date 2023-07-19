# Escopo de funções em Python
# Escopo significa o local onde aquele código pode atingir
# Existe o escopo global e local
# O escopo global é o escopo onde todo o código é alcançável 
# O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados


x = 1 # Esse x é diferente do x dentro da função

def escopo():
    global x
    x = 10
    
print(x)
escopo() # Depois de executar a função com x global, o x do escopo externo é alterado
print(x)

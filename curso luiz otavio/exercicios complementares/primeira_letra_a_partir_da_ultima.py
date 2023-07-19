nome = 'Jonathas'
quantidade_letra_nome = len(nome)
formula = -quantidade_letra_nome # Para pegar a primeira letra, começando da última, que seria -1
                                 # Basta deixar o len da string negativo
                                 # Outro exemplo seria como pegar a penúltima letra contando de trás pra frente
                                 # Nesse caso, bastaria somar +1 no tamanho da string.
print(nome[formula])

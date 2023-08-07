import pacote.operacoes
from pacote.numbergenerator import randomgenerator
from pacote import mostrarmsg

soma = pacote.operacoes.somar(1, 2)
subtracao = pacote.operacoes.subtrair(1, 3)
numero_aleatorio = randomgenerator(1, 10)

mostrarmsg.mostrarmsgnatela('Hello World')
print(soma, subtracao, numero_aleatorio)

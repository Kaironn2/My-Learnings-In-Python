numeros = range(10) # mostrar valores de 0 a 9, pois o python não lê o último valor
numeros = range(5, 10) # valores a partir do 5 até o 9
numeros = range(5, 10, 2) # o terceiro valor define o step, ou seja, de qnts em qnts valores vai pular
numeros = range(-1, -10, -1) # quando o step for negativo, o python só mostra valores do 0 pra baixo

for numero in numeros:
    print(numero)

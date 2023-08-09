from itertools import count

c1 = count(start=5, step=5)         # se argumentos não forem definidos, ele começará do 0 de 1 em 1.
                                    # Podemos definir o início e a quantidade de saltos também.
for i in c1:
    print(i)
    if i == 30:
        break

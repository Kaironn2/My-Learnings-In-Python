# Generator Functions
# generator = (n for n in range(1000000))
# O valor da função deve ser salvo em uma variável.
# Caso você fique executando a função várias vezes,
# ela começará do zero.
# Então, use o valor salvo na variável.

def generator(n=0):
    yield 1
    print('Continuando...')
    yield 2
    print('Continuando...')
    yield 3
    print('Acabou')


gen = generator()

print(next(gen))    # retorna 1
print(next(gen))    # retorna 2
print(next(gen))    # retorna 3


# generator com o for

def generator(n=0, maximum=20):
    while True:
        yield n
        n += 1

        if n >= maximum: # caso queira que o número pare no maximum definido, n > maximum
            return

gen = generator(n=5, maximum=11)

for n in gen:
    print(n)


# yield from

def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()
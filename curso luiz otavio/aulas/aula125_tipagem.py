# numero1: int | Dessa forma, tipamos o argumento, então ele terá que ser int

# numero1=1    | Dessa forma, definimos o valor padrão do argumento.
# Caso um valor não seja passado para ele, ele será 1

# Para tipar e definir um valor padrão, fazemos:
# numero1: int = 1

# Para definirmos o retorno de um método ou função, fazemos:
# def somar(numero1, numero2) -> int:
# Então o retorno sempre terá que ser int, ou apresentará um erro.

def somar(numero1: int = 1, numero2: int = 2) -> int:
    return numero1 + numero2

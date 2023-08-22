# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    ...


class OutroError(Exception):
    ...


def raise_error():
    exception_ = MyError('MENSAGEM DE ERROR')
    raise exception_


try:
    raise_error()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__, error)
    exception_ = OutroError('Esse é outro error.')
    raise exception_ from error

# try, except, else e finally

try:
    print('ABRIR ARQUIVO')          # primeira tentativa de execução
    8/0
except ZeroDivisionError as e:      # tratar erros
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:                               # Executar caso não haja erros
    print('Não deu erro')
finally:                            # Sempre será executado
    print('FECHAR ARQUIVO')

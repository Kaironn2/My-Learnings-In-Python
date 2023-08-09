import time

def medir_tempo(funcao):                # o decorator irá ter como parâmetro a função que será executada

    def wrapper(x, y):                  # o wrapper é definido logo após o decorator e terá nos parâmetros os parâmetros da função que será executada
                                        # que nesse caso é a função somar. Mas poderíamos passar *args, **kwargs para receber parâmetros variáveis de várias funções

        inicio = time.time()            # aqui decidimos o que será executado antes da função

        retornar = funcao(x, y)         # aqui chamamos o parâmetro função para executar a função que será passada

        fim = time.time()               # aqui decidimos o que faremos depois da execução da função
        tempo_passado = fim - inicio
        print(f'O tempo decorrido da função "{funcao.__name__}" foram {tempo_passado:.2f} segundos.')

        return retornar                 # Aqui, caso tenhamos guardado o return da função em um variável, retornaremos a variável
    
    return wrapper                      # e, por fim, retornaremos o wrapper

@medir_tempo                            # o decorator deve vir com um @ seguido de seu nome na linha anterior à definição da função
def soma(x, y):
    time.sleep(1)
    return x + y

somar = soma(3, 4)

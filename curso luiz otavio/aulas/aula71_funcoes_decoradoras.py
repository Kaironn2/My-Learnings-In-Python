import time

def medir_tempo(funcao):
    def decorator(*args, **kwargs):
        inicio = time.time()                # antes da execução
        resultado = funcao(*args, **kwargs) # execução
        fim = time.time()                   # depois da execução
        tempo_passado = fim - inicio
        print(f'A função {funcao.__name__} levou {tempo_passado:.2f} segundos para ser executada.')
        return resultado
    return decorator

@medir_tempo                                # decorator
def inverte_string(*args):
    for arg in args:
        if not isinstance(arg, str):
            raise ValueError(f"{arg} não é um string")
    
    time.sleep(2)  # Simulando uma operação demorada
    return [arg[::-1] for arg in args]

resultado = inverte_string("abc")
print('Resultado:', resultado)

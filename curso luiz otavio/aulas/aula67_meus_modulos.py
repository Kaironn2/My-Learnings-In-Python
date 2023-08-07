# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

try:
    import sys
    # import aula67_modulo_da_aula # Quando importado dessa forma, já é executado na importação
    from aula67_modulo_da_aula import jonathas
    sys.path.append(r'C:\Users\kaironn\Desktop\simulador')  # Importa um módulo de outro caminho
except ModuleNotFoundError:
    print('Módulo não encontrado.')

print('Este módulo se chama', __name__)
print(jonathas)

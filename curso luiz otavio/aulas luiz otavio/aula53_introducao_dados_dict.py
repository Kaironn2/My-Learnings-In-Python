# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor"
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro dicionário
# Usamos as chaves - {} ou a classe dict para criar dicionários
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

pessoa = {
 'nome': 'Luiz Otavio',
 'Sobrenome': 'Miranda',
 'idade': 18,
 'altura': 1.8,
 'endereços': [
           {'rua': 'tal tal', 'numero': 123},
           {'rua': 'outra rua', 'numero': 321},
           ]
       }

for item in pessoa:
    print(item, pessoa[item])

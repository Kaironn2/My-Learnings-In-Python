import json

# Json não suporta funções, métodos entre outras execuções

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},    # int -> number
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10), # tuple -> array
    'dev': True,        # True -> true
    'nada': None,       # None -> null
}

with open('aula82.json', 'w', encoding='utf8') as arquivo: # No windows, precisamos do econding=
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,         # Converte o arquivo mantendo acentos e outros caracteres. Por compatibilidade, é melhor manter a tabela ascii
        indent=2,       # Para melhor visibilidade, com essa identação ele tem as quebras de linha
    )

with open('aula82.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])
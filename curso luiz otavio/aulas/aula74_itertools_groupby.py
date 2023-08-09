from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

alunos_agrupados = sorted(alunos, key=lambda x: x['nota'])  # Primeiro ordenamos com a função sorted,
                                                            # nesse caso, ordenamos pela nota

grupos = groupby(alunos_agrupados, key=lambda x: x['nota']) # Depois agrupamos pela nota

for nota, grupo in grupos:                                  # A nota é o grupo, pois agrupamos pela nota
                                                            # e o grupo é o nome + nota    
                                                            
    print(nota)                                             # nesse print é mostrado o grupo, que são as notas

    for aluno in grupo:                                     # E aqui mostramos o nome e a nota do aluno.
        print(aluno)

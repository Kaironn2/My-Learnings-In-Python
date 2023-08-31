# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
# print(calendar.calendar(2022))
# print(calendar.month(2022, 12))
# numero_primeiro_dia, ultimo_dia = calendar.monthrange(2022, 12)
# print(list(enumerate(calendar.day_name)))
# print(calendar.day_name[numero_primeiro_dia])
# print(calendar.day_name[calendar.weekday(2022, 12, ultimo_dia)])

import calendar

# Para pegar o calendário de um ano específico:
print(calendar.calendar(2023))

# Para pegar o calendário de um mês específico de um ano específico:
print(calendar.month(2023, 8))

# Para saber o ultimo dia de um mês:
print('Ultimo dia de um mês:', calendar.monthrange(2023, 8))

# Nomes dos dias das semanas em seus respectivos índices:
days_list = list(calendar.day_name)
for i, day in enumerate(days_list):
    print(i, day, end=' - ')
print()

# Ultimo dia do mês com desempacotamento:
indice, ultimo_dia = calendar.monthrange(2023, 8)
dia_da_semana = calendar.day_name[indice]
print(f'O último dia do mês é {ultimo_dia} que será uma {dia_da_semana}')

# Mostrando todos os dias de um mês
for week in calendar.monthcalendar(2022, 12):
    for day in week:
        if day == 0:
            continue
        print(day)

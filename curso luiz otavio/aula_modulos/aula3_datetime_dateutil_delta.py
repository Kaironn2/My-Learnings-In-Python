from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
start_date = datetime.strptime('28/06/2023 15:04:36', fmt)
end_date = datetime.strptime('28/08/2023 16:00:00', fmt)
delta_dates = end_date - start_date  # delta de duas datas
delta = timedelta(days=10, hours=5)  # criando um timedelta
deltadateutil_ = relativedelta(start_date, end_date)

# Outra opção para trabalhar com deltatime. Diferente do timedelta do datetime,
# o relativatedelta tem mais opções.
delta_dateutil = (end_date + relativedelta(days=10, hours=5, minutes=50))

# retorna boolean
print('*' * 50)
print('Data inicial é maior que a final? ', start_date > end_date)
print('Data final é maior que a inicial? ', end_date > start_date)
print('As datas inicial e final são iguais? ', end_date == start_date)

# Retorna timedelta, a diferença entre as datas em dias. Caso não seja um dia
# completo, ele retornará a fração em horas.
print('*' * 50)
print('Diferença entre as datas, em dias e horas: ', delta)

# Caso você queira a diferença total em segundos
print('*' * 50)
print('Diferença total em segundos: ', delta.total_seconds())

# Diferença entre uma data e um timedelta:
print('*' * 50)
print('Diferença entre uma data e um timedelta: ', end_date - delta)

# Vendo diferenças de data de uma forma mais completa com o relativedelta
print('*' * 50)
print(deltadateutil_)

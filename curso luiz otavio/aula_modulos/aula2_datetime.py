# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

from pytz import timezone

#               ano/mes/dia hr/min/sec
data_str_data = '2022/04/20 07:49:23'
# data_str_data = '20/04/2022'
data_str_fmt = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('America/Bahia'))
data = datetime.strptime(data_str_data, data_str_fmt)
print(data)


# Horário atual do computador
print('*' * 50)
print('Horário atual do computador')
print(datetime.now())

# Horário atual timezone específica
print('*' * 50)
print('Horário atual, timezone específica: ')
print(datetime.now(timezone('America/Bahia')))

# Número de segundos - Era Unix - Podemos recriar datas usando esses segundos
print('*' * 50)
print('Recriando data a partir de segundos Era Unix: ')
print(datetime.fromtimestamp(1650423600.0))

# Para pegar o Unix Timestamp de uma data:
print('*' * 50)
print('Recriando data a partir de segundos Era Unix: ')
print(data.timestamp())

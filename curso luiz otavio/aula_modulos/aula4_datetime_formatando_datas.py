from datetime import datetime

# data = datetime(2023, 8, 29)
data = datetime.strptime('2023-08-29 12:23:59', '%Y-%m-%d %H:%M:%S')
print('Data antes da formatação:', data)

# Para formatar a data do jeito desejado:
fmt = '%d/%m/%Y %H:%M:%S'
print('*' * 50)
print('Data após a formatação:', data.strftime(fmt))

# Você pode formatar de várias formas:
# Apenas a data:
fmt = '%d/%m/%Y'
print('*' * 50)
print('Apenas a data:', data.strftime(fmt))

# Apenas as horas:
fmt = '%H:%M:%S'
print('*' * 50)
print('Apenas as horas:', data.strftime(fmt))

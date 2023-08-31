# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime

from dateutil.relativedelta import relativedelta

total_amount = 1_000_000
loan_date = datetime(2020, 12, 20)
years_diff = relativedelta(years=5)
final_date = loan_date + years_diff

installment_dates = []
installment_date = loan_date
while installment_date < final_date:
    installment_dates.append(installment_date)
    installment_date += relativedelta(months=+1)

num_installments = len(installment_dates)
installment_amount = total_amount / num_installments

for date in installment_dates:
    print(date.strftime('%d/%m/%Y'), f'R$ {installment_amount:,.2f}')

print()
print(
    f'You borrowed R$ {total_amount:,.2f} to be paid '
    f'over {years_diff.years} years '
    f'({num_installments} months) in installments of '
    f'R$ {installment_amount:,.2f}.'
)

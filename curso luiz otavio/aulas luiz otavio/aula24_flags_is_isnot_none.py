# None = Não valor
# is e is not = é ou não é (tipo, valor, identidade)
# flag = bandeira

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Mostre')
else:
    print('Não mostre')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

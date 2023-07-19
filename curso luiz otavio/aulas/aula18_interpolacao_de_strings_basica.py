# Interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABDCEF0123456789)

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' %(nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' %(1500, 1500)) # 08 -> irá preencher as casas que faltarem para completar
                                                  # as 8 casas com zeros. X maiúsculo para hexadecimal maiúsculo
                                                  # x minúsculo para hexadecimal minúsculo
                                                  
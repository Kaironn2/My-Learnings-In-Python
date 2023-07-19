taxa_pagueveloz_brn_1x = 3.74  / 100
taxa_pagueveloz_brn_2x = 4.90 / 100
taxa_pagueveloz_brn_3x = 5.53 / 100
taxa_pagueveloz_brn_4x = 6.22 / 100
taxa_pagueveloz_brn_5x = 6.29 / 100
taxa_pagueveloz_brn_6x = 7.56 / 100
taxa_pagueveloz_brn_7x = 8.35 / 100
taxa_pagueveloz_brn_8x = 9.00 / 100
taxa_pagueveloz_brn_9x = 9.55 / 100
taxa_pagueveloz_brn_10x = 9.65 / 100
taxa_pagueveloz_brn_11x = 11.19 / 100
taxa_pagueveloz_brn_12x = 11.33 / 100


taxa_pagueveloz_1x = 5.11 / 100
taxa_pagueveloz_2x = 6.02 / 100
taxa_pagueveloz_3x = 6.83 / 100
taxa_pagueveloz_4x = 7.63 / 100
taxa_pagueveloz_5x = 8.41 / 100
taxa_pagueveloz_6x = 9.19 / 100
taxa_pagueveloz_7x = 10.24 / 100
taxa_pagueveloz_8x = 11.00 / 100
taxa_pagueveloz_9x = 11.75 / 100
taxa_pagueveloz_10x = 12.49 / 100
taxa_pagueveloz_11x = 13.22 / 100
taxa_pagueveloz_12x = 13.95 / 100


taxa_moderninhapro_master_visa_1x = 3.74 / 100
taxa_moderninhapro_master_visa_2x = 4.90 / 100
taxa_moderninhapro_master_visa_3x = 5.53 / 100
taxa_moderninhapro_master_visa_4x = 6.22 / 100
taxa_moderninhapro_master_visa_5x = 6.29 / 100
taxa_moderninhapro_master_visa_6x = 7.56 / 100
taxa_moderninhapro_master_visa_7x = 8.35 / 100
taxa_moderninhapro_master_visa_8x = 9.00 / 100
taxa_moderninhapro_master_visa_9x = 9.55 / 100
taxa_moderninhapro_master_visa_10x = 10.25 / 100
taxa_moderninhapro_master_visa_11x = 10.89 / 100
taxa_moderninhapro_master_visa_12x = 11.48 / 100


taxa_moderninhapro_demaisbandeiras_1x = 4.74 / 100
taxa_moderninhapro_demaisbandeiras_2x = 5.98 / 100
taxa_moderninhapro_demaisbandeiras_3x = 6.67 / 100
taxa_moderninhapro_demaisbandeiras_4x = 7.36 / 100
taxa_moderninhapro_demaisbandeiras_5x = 8.06 / 100
taxa_moderninhapro_demaisbandeiras_6x = 8.75 / 100
taxa_moderninhapro_demaisbandeiras_7x = 10.19 / 100
taxa_moderninhapro_demaisbandeiras_8x = 10.87 / 100
taxa_moderninhapro_demaisbandeiras_9x = 11.56 / 100
taxa_moderninhapro_demaisbandeiras_10x = 12.25 / 100
taxa_moderninhapro_demaisbandeiras_11x = 12.93 / 100
taxa_moderninhapro_demaisbandeiras_12x = 13.60 / 100



print('INFORME O VALOR TOTAL FINANCIADO: ')
print('ex -> 2000.60\n')

valor_financiado:.3 = float(input('R$'))



print('\nINFORME O VALOR RECEBIDO DO CLIENTE')

valor_recebido_cliente = float(input('R$'))



print('\nAGORA INFORME A QUANTIDADE DE PARCELAS')
print('obs: apenas números inteiros, ex -> 10\n')

quantidade_parcelas = int(input('Quantidade de parcelas: '))



print('INFORME EM QUAL INSTITUIÇÃO FOI A OPERAÇÃO:\n ')

print('1 - PagueVeloz Brn                   ')
print('2 - Moderninha Pro MASTER e VISA     ')
print('3 - Moderninha Pro Demais Bandeiras  ')
print('4 - Pagueveloz                       ')

opcao = int(input('\nDigite o número correspondente à opção desejada: '))

while True:

    if opcao >= 1 and opcao <= 4:
        break
    
    print('\nA opção digitada não é válida, por favor, selecione uma das opções listadas.')

    opcao = int(input('\nDigite o número correspondente à opção desejada: '))



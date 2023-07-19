lista_produtos = []
lista_preco_produtos = []
import os

while True:
    print(
        '\n[i] - inserir\n'
        '[a] - apagar\n'
        '[l] - listar\n'
        '[s] - sair')
    
    while True:
        opcao = input('\nInforme a opção desejada: ').lower()
        print()

        if opcao == '':
            continue

        if opcao[0] in 'ials':
            break
        
        else:
            print('Por favor, selecione uma opção válida.\n')

    if opcao[0] == 's':
        print('\nPrograma finalizado.')
        break

    elif opcao[0] == 'i':
        while True:
            os.system('cls')
            produto = input('Digite o nome do produto: ')
            preco_produto = float(input('Digite o valor do produto: R$'))
            lista_produtos.append(produto)
            lista_preco_produtos.append(preco_produto)

            sair_insercao = input('Você deseja cadastrar outro produto? [s]im [n]ão: ').lower().startswith('n')
            

            if sair_insercao:
                break
    
    elif opcao[0] == 'a':
        while True:
            apagar = input('\nInforme o índice do produto que você quer apagar: ')
            
            try:
                apagar = int(apagar)
                print(f'O produto {lista_produtos[apagar]} foi apagado com sucesso.')
                lista_produtos.pop(apagar)
                lista_preco_produtos.pop(apagar)
                
            except ValueError:
                print('Por favor, digite um número inteiro.')
            except IndexError:
                print('O índice digitado não está na lista.')

            sair_apagar = input('\nVocê deseja apagar outro produto? [s]im [n]ão: ').lower().startswith('n')

            if sair_apagar:
                os.system('cls')
                break
                
            os.system('cls')
            for indice, produto in enumerate(lista_produtos):
                print(f'{indice} - - - - - - {produto} - - - - - - - - R${lista_preco_produtos[indice]}')

    elif opcao[0] == 'l':
        os.system('cls')

        if lista_produtos == []:
            print('Ops, sua lista está vazia :(. Primeiro adicone um item.')

        else:
            for indice, produto in enumerate(lista_produtos):
                print(f'{indice} - - - - - - {produto} - - - - - - - - R${lista_preco_produtos[indice]}')

# if  /    elif   / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar': # o if pode trabalhar sozinho
    print('Você entrou no sistema.')

elif entrada == 'sair': # o elif só funciona se primeiramente houver um if 
    print('Você saiu do sistema.')

       # o else só funciona se houver um if, e caso nenhuma das
else:  #condições anteriores sejam atendidas, vai executar o else
    print('Você digitou uma opção inválida.')

# Somente uma condição do bloco de if será executada
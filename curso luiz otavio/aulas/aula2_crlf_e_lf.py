from time import sleep  # Importação de módulos será explicada mais adiante

# Estaremos usando o comando sleep() do módulo time entre cada exemplo para ter um intervalo de 2 segundos
# entre cada exemplo na tela.

# Se usarmos o argumento end='', poderemos definir o que acontecerá ao chegar no final da ação.
# Por padrão, o que vem definido no final da linha é end='\r\n', que serve para retornar o cursor
# para o início da linha e passar para a próxima linha, ou seja, quando ele chega no final da linha
# ele passa a para o início da próxima. Como é o padrão dele, não é necessidade de deixá-lo explicito.
# Mas por exemplo, se quiséssemos que quand que chegasse ao fim da linha, ele juntasse a próxima linha
# faríamos assim:

print('------EXEMPLO 1------')
print('Essa é a mensagem da primeira linha ', end='')
print('Essa é a segunda mensagem')
print()  # Como por padrão, end='\r\n, então, um print vazio serve para pular uma linha.'

# Caso queiramos, podemos botar qualquer outra coisa no final da linha, por exemplo,
# se quisessemos separar as linhas apenas por uma barra, invés de quebrar a linha:

sleep(2)
print('------EXEMPLO 2------')
print('Essa é a mensagem da primeira linha ', end='/')
print('Essa é a mensagem da segunda linha')
print()

# \r - CARRIAGE RETURN -> Em linguagens de programação, incluindo python,
# é um caractere que serve para quando identificado, retorne o cursor para o início da linha.
# Então, sempre que o cursor encontrar um caractere \r, ele retornará para o início da linha
# e escreverá o próximo texto na mesma linha, sobrescrevendo a linha antiga.

# Por exemplo, nessa linha de código, apenas a "Mensagem Número 2" seria mostrado na tela,
# pois quando o cursor chegasse no \r, ele voltaria a o início da linha, sobrescrevendo o que vem
# a "A Mensagem número 1".

sleep(2)
print('------EXEMPLO 3------')
print('Mensagem número 1\rMensagem Número 2')
print()

# Uma das utilidades para o \r seria a função sleep, que serve para definir um intervalo entre uma ação e outra,
# Por exemplo, se definisse um sleep(2), haveria um intervalo de 2 segundo até a próxima ação. Por exemplo:

sleep(2)
print('------EXEMPLO 4------')
print('Essa mensagem será sobrescrevida', end='\r')
sleep(2)
print('A mensagem anterior foi sobrescrevida')
print()

# É importante ressaltar que o caractere \r faz o cursor voltar para o início da linha.
# Então, se houver outra mensagem anterior, que seja maior que a sucessora, ela só sobrescreverá
# a mesma quantidade de caracteres que há na sucessora, e o resto da anterior permanecerá.
# Por exemplo, definissimos duas mensagem, a primeira sendo: '1234' e a segunda sendo '345',
# o nosso retorno seria 3454, pois o 4 da primeira mensagem não seria sobrescrevido, por conta
# da primeira mensagem possuir 4 caracteres, e a segunda só possuir 3. Então, a mensagem sucessor
# irá sobrescrever os 3 primeiros caracteres, e do 4° caractere em diante, ainda continuaria sendo mostrado.
# O que você poderia fazer para sobrescrever a mensagem por completa, seria pôr espaços vazios no fim, ex:

sleep(2)
print('------EXEMPLO 5------')
print('1234', end='\r')
sleep(2)
print('345 ')
print()


# \n - NEW LINE -> Já o caractere \n, representa uma quebra de linha, ou seja, quando encontrado
# a linha será quebrada, passando para próxima linha.
# Atualmente, quando usamos o caractere \n, após a quebra de linha, o cursor já volta pro início da linha.

# Por exemplo, no trecho de código a seguir, se quisessemos escrever duas mensagens, uma em cada linha,
# em um único print, poderíamos usar o \n, dessa forma:

sleep(2)
print('------EXEMPLO 6------')
print('Primeira linha\nSegunda Linha')
print()

sleep(2)
print('------EXEMPLO 7------')
print('Primeira linha\nSegunda Linha', sep='')

# RESUMO
# \r\n -> CRLF(Carriage Return Line Feed) - Windows - Quebra de linha
# \n -> LF(Line Feed) - Linux, Mac - Quebra de linha
# end='' serve para trocar a quebra de linha do final da linha por outra coisa.

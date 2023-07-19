a = 'A'
b = 'B'
c = 1.1

# Tudo que tem uma ordem, começa no índice zero
# Então, o primeiro elemento da ordem sempre vai ser o número 0
# Se tem 3 elementos, eles serão respetivamente: 0, 1 e 2

string = 'a={2} b={1} c={0}' # Você pode mudar a ordem da formatação puxando pelo índice
formatar = string.format(a, b , c)

str = 'a={q} b={w} c{e}' # Você também pode nomear as variáveis que serão foramtadas
format = str.format(q=a, w=b, e=c)

print(formatar)

# erro OUT OF RANGE, você está buscando algo que já acabou. 
# Por exemplo, tentar adicionarr uma 4 formatação, sendo que só tem 3 chaves

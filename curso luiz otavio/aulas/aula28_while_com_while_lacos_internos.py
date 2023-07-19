# While (equanto)
# Executa uma ação enquanto uma condição for verdadeira 
# Loop infinito -> código sem fim

quantidade_linhas = 5
quantidade_colunas = 5

linha = 1

while linha <= quantidade_linhas:

    coluna = 1

    while coluna <= quantidade_colunas:
        print(linha, coluna)
        coluna += 1

    linha += 1

print('Fim')

# Imutáveis vistas: str, bool, int, float
# Você não consegue atribuir um novo valor a um tipo imutável,
# precisa criar uma variável nova.

string = "jonathas barros"
string_modificada = f'{string[:6]}an{string[8:12]}bosa'
print(string_modificada.title())

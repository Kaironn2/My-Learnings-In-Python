# O operador or irá avaliar a expressão e parar no primeiro valor verdadeiro

print(True or False or False) # retornará True e não avaliará mais nenhuma condição
print(False or False or True) # como o valor verdadeiro está como última condição, 
                              #toda expressão será avaliada

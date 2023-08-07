# Módulos no python são singleton
# ou seja, só vão ser carregados uma vez,
# exceto que você exija que recarregue ele.
# Para recarregar o módulo, usamos importlib.reload()

import importlib

import aula67_modulo_da_aula


for i in range(10):
    importlib.reload(aula67_modulo_da_aula)

print('Acabou')

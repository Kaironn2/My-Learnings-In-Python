class Pessoa:
    def __init__(self, nome, sobrenome):    # primeiro parâmetro reservado pro self
        self.nome = nome    # atributo
        self.sobrenome = sobrenome  # atributo


pessoa1 = Pessoa('Maria', 'Barros')

pessoa2 = Pessoa('Carla', 'Oliveira')

print(pessoa1.nome, pessoa1.sobrenome)
print(pessoa2.nome, pessoa2.sobrenome)

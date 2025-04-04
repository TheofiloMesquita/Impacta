class Pessoa:
    def __init__(self, nome, idade, end):
        self.nome = nome
        self.idade = idade
        self.end = end

    def set_alterar(self, end):
        self.end = end

    def exibir():
        print(pessoa.nome, pessoa.idade, pessoa.end)

pessoa = Pessoa("caio", 2, "SP")
print(pessoa.nome)
print(pessoa.idade)
print(pessoa.end)

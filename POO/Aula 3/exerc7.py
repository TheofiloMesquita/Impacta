class Evento:
    def __init__(self, nome, data, convidados):
        self.nome = nome
        self.data = data
        self.convidados = convidados

    def alterar(self, data):
        self.data = data

    def exibir(self):
        print(self.nome, self.data, self.condidados)

festa = Evento("praia", "01/01/2026", 5)
print(festa.nome)
print(festa.data)
print(festa.convidados)

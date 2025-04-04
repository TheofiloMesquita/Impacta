class Sala:
    def __init__(self, numero):
        self.sala = numero

class Edificio:
    def __init__(self, nome):
        self.nome = nome
        self.salas = []

    def adicionar_quarto(self, numero):
        self.salas.append(numero)

predio = Edificio("Perim")
print(predio.nome)
print(predio.salas)
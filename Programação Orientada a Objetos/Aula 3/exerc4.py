class Carro:
    def __init__(self, marca, modelo, ano, km):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.km = km

    def dirigir(self, km):
        self.km += km

    def exibir(self):
        print(carro.nome, carro.marca, carro.modelo, carro.ano, carro.km)

carro = Carro("BMW", "i7", 2025, 0)
print(carro.marca)
print(carro.modelo)
print(carro.ano)
print(carro.km)

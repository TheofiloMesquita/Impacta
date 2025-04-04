class Animal:
    def __init__(self, nome, cor, numero_de_patas):
        self.nome = nome
        self.cor = cor
        self.numero_de_patas = numero_de_patas
    
    def exibir_dados(self):
        print(self.nome, self.cor, self.numero_de_patas)

class Cachorro(Animal):
    def __init__(self, nome, cor, numero_de_patas, raca):
        super().__init__(nome, cor, numero_de_patas)
        self.raca = raca

    def exibir_dados(self):
        print(self.nome, self.cor, self.numero_de_patas, self.raca)

animal = Animal("Passarinho", "Azul", 2)
animal.exibir_dados() # exibe os atributos do animal

dog = Cachorro("Rex", "Marrom", 4, "Vira lata")
dog.exibir_dados() # exibe os atributos do cachorro
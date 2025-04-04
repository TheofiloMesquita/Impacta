class AnimalDeEstimacao:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def mudarIdade(self, idade):
        if(idade > 0):
            self.idade = idade

pet = AnimalDeEstimacao("cachorro", "Rusky", 2)
print(pet.nome)
print(pet.especie)
print(pet.idade)

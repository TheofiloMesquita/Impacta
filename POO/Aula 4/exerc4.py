class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        if(idade > 0):
            self.__idade = idade
        else:
            self.__idade = 0
            print("Insira um valor de idade real")

p1 = Pessoa("caio", 20)
print(p1.idade)

p1.idade = -2

p1.idade = 21
print(p1.idade)
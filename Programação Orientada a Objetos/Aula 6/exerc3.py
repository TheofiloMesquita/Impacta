class Animal:
    contador = 0
    def __init__(self, nome):
        self.animais = []
        self.animais.append(nome)
        Animal.incrementador()
    
    @classmethod
    def incrementador(cls):
        cls.contador +=1

    @classmethod
    def quantidade_instancias(cls):
        return cls.contador
    
    @staticmethod
    def mensagem_sobre_animais():
        print("Animais são seres vivos!")


cachorro = Animal("Rex")
gato = Animal("Mimi")
print(Animal.quantidade_instancias()) # Saída: 2
Animal.mensagem_sobre_animais() # Saída: "Animais são seres vivos!"
class Professor:
    def __init__(self, nome, disciplina=[]):
        self.nome = nome
        self.disciplina = disciplina 
    
class Disciplina:
    def __init__(self, nome):
        self.nome = nome

materia = Disciplina("matematica")
print(materia.nome)

p1 = Professor("Caio", ["matematica", "Inglês", "portugues"])
print(p1.disciplina)
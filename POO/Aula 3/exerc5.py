class Aluno:
    def __init__(self, nome, ra, curso):
        self.nome = nome
        self.ra = ra
        self.curso = curso

    def trocar(self, curso):
        self.curso = curso

    def exibir(self):
        print(Aluno.nome, Aluno.ra, Aluno.curso)

aluno = Aluno("caio", "123456789", "SI")
print(aluno.nome)
print(aluno.ra)
print(aluno.curso)

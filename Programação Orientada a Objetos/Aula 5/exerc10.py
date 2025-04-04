class Medico:
    def __init__(self, nome, idade, especialidade, lista):
        self.nome = nome
        self.idade = idade
        self.especialidade = especialidade
        self.lista = lista

    def exibir_pacientes(self):
        print(self.nome, self.idade, self.especialidade, self.lista)

    def media_idade_pacientes(self):
        media = 0
        divisor = 0
        for i in range(len(self.lista)):
            media += self.lista[i][1]
            divisor += 1
        print(f'A media da idade dos pacientes é {media/divisor}')

class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

medico1 = Medico("Dereck Shappard", 30, "Neurologia", [["Jorge Cluney", 30],["Pernalonga", 25]])
medico1.exibir_pacientes()
medico1.media_idade_pacientes()

paciente0 = Paciente("Arnold", 12)
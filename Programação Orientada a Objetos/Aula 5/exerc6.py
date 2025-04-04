class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_funcionario = []

    def contratar(self, funcionario):
        self.lista_de_funcionario.append(funcionario)

class Funcionario:
    def __init__(self, nome):
        self.nome = nome

p1 = Funcionario("caio")
print(p1.nome)

d1 = Departamento("RH")
contrato = Departamento.contratar = "caio"
print(f'Contratamos o {p1.nome}, para o cargo {d1.nome}')
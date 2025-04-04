class Funcionario:
    def __init__(self, nome, dt, sexo, salario, end):
        self.nome = nome
        self.dt = dt
        self.sexo = sexo
        self.salario = salario
        self.end = end

    def exibir_dados(self):
        print(self.nome, self.dt, self.sexo, self.salario, self.end)

class Endereço:
    def __init__(self, rua, numero, bairro, complemento, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.complemento = complemento
        self.cep = cep

    def exibir_dados(self):
        print(self.rua, self.numero, self.bairro, self.complemento, self.cep)

funcinario1 = Funcionario("ithalo", "12/01/2000", "M", 2000, "Brooklyn")
funcinario1.exibir_dados()

end1 = Endereço("coração de ouro", 123, "Vila Carmezin", "Casa branca", "02585-901")
end1.exibir_dados()
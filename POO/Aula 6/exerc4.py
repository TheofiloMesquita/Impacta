from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def calcularSalario():
        pass

class FuncionarioCLT(Funcionario):
    def __init__(self, nome, idade, salario_bruto, dependentes):
        self.nome = nome
        self.idade = idade
        self.salario = salario_bruto
        self.dependentes = dependentes

    def calcularSalario(self):
        dependente = self.dependentes * 190
        vt = 0.06 * self.salario #Vale Transporte
        if(self.salario < 1700):
            INSS = 0.08 * self.salario #Previdência Social
            IR = 0.075 * self.salario #Imposto de Renda
            self.salario = self.salario - vt - INSS - IR - dependente
        elif(self.salario < 2800):
            INSS = 0.09 * self.salario
            IR = 0.075 * self.salario
            self.salario = self.salario - vt - INSS - IR - dependente
        elif(self.salario < 5600):
            if(self.salario < 3800):
                INSS = 0.11 * self.salario
                IR = 0.15 * self.salario
                self.salario = self.salario - vt - INSS - dependente
            elif(self.salario < 4700):
                INSS = 0.11 * self.salario
                IR = 0.225 * self.salario
                self.salario = self.salario - vt - INSS - dependente
            else:
                INSS = 0.11 * self.salario
                IR = 0.275 * self.salario
                self.salario = self.salario - vt - INSS - dependente
        print(f'O funcionario ganha com descontos ${self.salario}')
    
class FuncionarioPJ(Funcionario):
    def __init__(self, nome, idade, salario_bruto):
        self.nome = nome
        self.idade = idade
        self.salario = salario_bruto
        
    def calcularSalario(self):
        IRPJ = 0.15 #Imposto de Renda de Pessoa Juridica
        CSLL = 0.09 #Contribuição sobre o lucro liquido obitido
        PIS_Confins = 0.0365 #Seguro desemprego
        INSS = 0.2 #Previdência Social ***Opcional***
        DAS = 0.045 - 0.33 #Documento de arrecadação do Simples Nacional Ou seja paga o titulo de PJ
        ISS = 0.02 - 0.05 #Imposto sobre serviços

        print(f'O funcionario {self.nome} tem {self.idade} anos e ganha sem descontos ${self.salario}')

funcionario1 = FuncionarioCLT("Carlos", 30, 5000, 2)
funcionario1.calcularSalario()

funcionario2 = FuncionarioPJ("Ana", 28, 8000)
funcionario2.calcularSalario()
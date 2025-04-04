class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        Pessoa.set_idade(self, idade)

    def set_idade(self, idade):
        while True:
            if(idade < 18):
                print("Insira uma idade valida")
                idade = int(input())
            else:    
                self.idade = idade
                break

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        self.__salario = salario
        super().__init__(nome, idade)
    
    @property
    def get_salario(self):
        return self.__salario
    
    @get_salario.setter
    def set_salario(self, salario):
        self.__salario = salario
    
    def calcular_salario_anual(self):
        print(f'O funcionário {self.nome} recebe por ano {12*self.__salario}')
        return 12*self.__salario

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_funcionarios = []
    
    def adicionar_funcionario(self, lista):
        self.lista_de_funcionarios.append(lista)
    
    def calcular_total_salarios(self):
        gasto_anual = 0
        for i in range(len(self.lista_de_funcionarios)):
            gasto_anual += self.lista_de_funcionarios[i][2]*12
        print(f'O total gasto com salarios anualmente é de {gasto_anual}')
    
    def listar_funcionarios(self):
        for i in range(len(self.lista_de_funcionarios)):
            print(f'{self.lista_de_funcionarios[i][0]} recebe por ano {self.lista_de_funcionarios[i][2]*12}')

pessoa1 = Pessoa("Claudia", 30)

funcionario1 = Funcionario("Ingrid", 28, 20000)
funcionario2 = Funcionario("Priscila", 40, 18000)
funcionario3 = Funcionario("Rafaela", 17, 15000)

departamento1 = Departamento("Banco")
departamento1.adicionar_funcionario(["Ingrid", 28, 20000])
departamento1.adicionar_funcionario(["Priscila", 40, 18000])
departamento1.adicionar_funcionario(["Rafaela", 17, 15000])

departamento1.listar_funcionarios()

departamento1.calcular_total_salarios()
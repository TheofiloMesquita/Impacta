class Motor:
    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia
        
class veiculo:
    def __init__(self, ano, preco, motor):
        self.ano = ano
        self.preco = preco
        self.motor = motor

class Carro(veiculo):
    def __init__(self, ano, preco, motor, cor, modelo):
        super().__init__(ano, preco, motor)
        self.cor = cor
        self.modelo = modelo
    
    def exibir_dados(self):
        print(self.ano, self.preco, self.motor, self.cor, self.modelo)

class Caminhao(veiculo):
    def __init__(self, ano, preco, motor, comprimento):
        super().__init__(ano, preco, motor)
        self.comprimento = comprimento
    
    def exibir_dados(self):
        print(self.ano, self.preco, self.motor, self.comprimento)

motor1 = Motor(1000, 500)
motor2 = Motor(8000, 900)
carro = Carro(2010, 20000, motor1, "branca", "gol")
caminhao = Caminhao(2015, 80000, motor2, 10)
carro.exibir_dados()
# imprime os valores de todos os atributos do carro
caminhao.exibir_dados()
# imprime os valores de todos os atributos do caminhão
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @classmethod
    def mensagem_manutencao(cls):
        print('Faça a manutenção regular do seu veículo!')

class Carro(Veiculo):
    def ligar(self):
        print('Carro ligado com a chave')

class Moto(Veiculo):
    def ligar(self):
        print('Moto ligada com partida elétrica')

carro = Carro()
moto = Moto()
carro.ligar() # Saída: "Carro ligado com chave"
moto.ligar() # Saída: "Moto ligada com partida elétrica"
Veiculo.mensagem_manutencao()
# Saída: "Faça a manutenção regular do seu veículo!"
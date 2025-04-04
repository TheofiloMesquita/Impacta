class ContaBancaria:
    def __init__(self, titular, conta, saldo):
        self.nome = titular
        self.conta = conta
        self.saldo = saldo

    def depositar(self, saldo):
        if(saldo > 0):
            self.saldo += saldo

    def sacar(self, saldo):
        if(saldo > 0 and saldo < saldo):
            self.saldo = saldo

    def detalhes(self):
        print(self.titular, self.conta, self.saldo)

conta = ContaBancaria("Caio", "00123456789", 100000)
print(conta.nome)
print(conta.conta)
print(conta.saldo)

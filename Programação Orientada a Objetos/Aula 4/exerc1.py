class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = 0
        self.set_depositar(saldo)

    def get_extrato(self):
        return self.__saldo
    
    def set_depositar(self, saldo):
        if(saldo > 0):
            self.__saldo += saldo



NuBank = ContaBancaria(2000)
print(NuBank.get_extrato())

NuBank.set_depositar(500)
print(NuBank.get_extrato())
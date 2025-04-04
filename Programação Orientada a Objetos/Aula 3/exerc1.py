class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        
    def set_adicionar(self, qtd):
        if (qtd > 0):
            self.qtd += qtd

    def set_remover(self, qtd):
        if(qtd > 0 and qtd < qtd):
            self.qtd -= qtd
        else:
            print("Insira um numero positivo")

loja = Produto("bala", 2, 20)
print(loja.nome)
print(loja.preco)
print(loja.qtd)

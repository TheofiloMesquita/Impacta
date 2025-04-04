class Lampada:
    def __init__(self, estado):
        self.estado = estado
    
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado

comodo = Lampada("ligado")
print(comodo.estado)

comodo.estado = "desligado"
print(comodo.estado)

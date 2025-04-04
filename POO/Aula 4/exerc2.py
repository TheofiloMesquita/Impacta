class Lampada:
    def __init__(self):
        self.__estado = "desligado"

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        if(self.__estado == "ligado" and estado == "desligado"):
            self.__estado = estado
        elif(self.__estado == "desligado" and estado == "ligado"):
            self.__estado = estado
        else:
            print("não tente acender a lâmpada que ja esta acesa ou apagar a lâmpada que ja esta apagada")

comodo = Lampada()
print(comodo.get_estado())

comodo.set_estado("ligado")
print(comodo.get_estado())

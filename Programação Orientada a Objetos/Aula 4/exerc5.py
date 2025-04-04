class Circulo:
    def __init__(self, raio):
        self.raio = raio

    @property
    def raio(self):
        return self.__raio
    
    @raio.setter
    def raio(self, raio):
        if(raio > 0):
            self.__raio = raio
        else:
            print("Insira um valor de raio real")
        
    @property
    def area(self):
        return (3.14 * self.raio ** 2)

rodaGigante = Circulo(2.5)
print(rodaGigante.area)
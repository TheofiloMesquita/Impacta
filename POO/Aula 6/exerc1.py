from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    
    @abstractmethod
    def calcularArea(self):
        pass

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        print(self.raio**2 * 3.14)

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        print(self.base * self.altura)

forma1 = Circulo(5)
forma1.calcularArea()

forma2 = Retangulo(2,5)
forma2.calcularArea()
class Calculadora:
    def __init__(self):
        pass

    @staticmethod
    def somar(valor1, valor2):
        return valor1 + valor2
    
    @staticmethod
    def subtrair(valor1, valor2):
        return valor1 - valor2
    
    @staticmethod
    def multiplicar(valor1, valor2):
        return valor1 * valor2
    
    @staticmethod
    def dividir(valor1, valor2):
        return valor1 / valor2
    
print(f"O resultado da soma de 4 + 5 é {Calculadora.somar(4,5)}")
print(f"O resultado da subtração de 7 - 2 é {Calculadora.subtrair(7,2)}")
print(f"O resultado da multiplicação de 5 * 12 é {Calculadora.multiplicar(5,12)}")
print(f"O resultado da divisão de 244 / 10 é {Calculadora.dividir(244,10)}")
from abc import ABC, abstractclassmethod

class Calculadora(ABC):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    @abstractclassmethod
    def calculo(self):
        pass


class Soma(Calculadora):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)

    def calculo(self):
        print('Resultado da soma: {}'.format(self.n1 + self.n2))


class Subtracao(Calculadora):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)

    def calculo(self):
        print('Resultado da subtração: {}'.format(self.n1 - self.n2))


soma = Soma(5, 1)
subtracao = Subtracao(10, 2)
calculos = [soma, subtracao]

for c in calculos:
    c.calculo()
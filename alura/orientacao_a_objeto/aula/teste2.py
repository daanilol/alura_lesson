
class Calculadora:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.soma = 0
        self.subtracao = 0
        self.multiplicacao = 0
        self.divisao = 0
 
 
    def somar(self):
        self.soma = self.x + self.y
        return self.soma


    def subtrair(self):
        self.subtracao = self.x - self.y
        return self.subtracao


    def multiplicar(self):
        self.multiplicacao = self.x * self.y
        return self.multiplicacao


    def dividir(self):
        self.divisao = self.x / self.y
        return self.divisao

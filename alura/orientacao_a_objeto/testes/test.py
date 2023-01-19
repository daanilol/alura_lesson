

class Tabuada:
    def __init__(self):
        self.number = int(input('Digite um número para efetuar o calculo: '))
        self.list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    def calculator(self):                
        for n in range(11):
            self.result = self.number * n
            print('{} x {} = {}'.format(self.number, n, self.result))


tab = Tabuada()
tab.calculator()



class Teste:
    def __init__(self, valor):
        self.x = valor
    
    '''Método getter para retornar o valor do atributo x'''
    def get_valor(self):
        return self.x
    
    '''Método setter para atribuir um novo valor ao atributo x'''
    def set_valor(self, v):
        self.x = v


teste = Teste(10)
print(teste.get_valor())

val = int(input('Digite um valor numérico: '))
teste.set_valor(val)
print(teste.get_valor())
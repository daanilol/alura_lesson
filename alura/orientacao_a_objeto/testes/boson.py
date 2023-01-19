
class Teste:
    def __init__(self, valor):
        self.x = valor


    def get_valor(self):
        '''Método getter para retornar o valor do atributo x'''
        return self.x


    def set_valor(self, valor):
        '''Método setter para atribuir um novo valor ao atributo x'''
        self.x = valor


teste = Teste(10)
print("Valor do Objeto:", teste.get_valor())

valor = int(input("Digite um valor número: "))
teste.set_valor(valor)

print("Valor do Projeto após a atribuição", teste.get_valor())

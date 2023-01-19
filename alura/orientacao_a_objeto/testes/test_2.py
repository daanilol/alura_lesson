

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def desconto(self, percentual):
        self.preco = (percentual / 100) * self.preco

    #get
    @property
    def preco(self):
        return self._preco

    #setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


produto = Produto('CAMISETA', 500)
produto.desconto(10)
print(produto.preco)

produto_2 = Produto('CARRO', 'R$55000')
produto_2.desconto(10)
print(produto_2.preco)
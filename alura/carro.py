from abc import ABC, abstractmethod
from enum import Enum, auto


class Carro(ABC):
    def __init__(self, nome, marca):
        self.__nome = nome
        self.__marca = marca


    @abstractmethod
    def nome_e_marca(self):
        pass


    @property
    def nome(self):
        return self.__nome


    @property
    def marca(self):
        return self.__marca



class Ferrari(Carro):
    def __init__(self, nome, marca, preco):
        super().__init__(nome, marca)
        self.preco = preco

    def nome_e_marca(self):
        print("Nome: {}, Marca: {}, Preço: {}".format(self.nome, self.marca, self.preco))


class Gol(Carro):
    def __init__(self, nome, marca, preco, ano):
        super().__init__(nome, marca)
        self.preco = preco
        self.ano = ano

    def nome_e_marca(self):
        print("Nome: {}, Marca: {}, Preço: {}, Ano: {}".format(self.nome, self.marca, self.preco, self.ano))



carro = Ferrari('gst600', 'ferrari', 12345678)
carro.nome_e_marca()


carro2 = Gol('gol 1', 'volks', 900, 1999)
carro2.nome_e_marca()
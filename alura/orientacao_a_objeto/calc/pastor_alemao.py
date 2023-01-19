from cachorro import *


class PastorAlemao(Cachorro):
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def info(self):
        print(f'Nome: {self.nome} Raça: {self.raca}')


c = PastorAlemao("zé", "pastor alemao")
c.info()
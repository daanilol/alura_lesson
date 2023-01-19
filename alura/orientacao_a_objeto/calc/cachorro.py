from abc import ABC,abstractmethod


class Cachorro(ABC):
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    @abstractmethod
    def info(self):
        pass
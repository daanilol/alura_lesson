from enum import Enum

class Cargo(Enum):
    TECNICO = 0
    CHEFE = 1
    SUPERVISOR = 1
    COORDENADOR = 1


class Licenca(Enum):
    E1 = 0
    E3 = 1


class Cliente: #classe
    def __init__(self, cliente, matricula, setor, cargo): #método construtor(parâmetros)
        self.__cliente = cliente  #atributo, argumento
        self.__matricula = matricula
        self.__setor = setor
        self.__cargo = cargo


    @property
    def licenca(self):
        if self.__cargo == Cargo.TECNICO:
            return Licenca.E1
        else:
            return Licenca.E3

    @property
    def cliente(self):
        return self.__cliente

    @property
    def matricula(self):
        return self.__matricula


    def setor(self):
        return self.__setor


    @property
    def cargo(self):
        return self.__cargo


    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo


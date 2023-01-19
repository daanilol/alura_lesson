from abc import ABC, abstractmethod
from enum import Enum, auto


class Color(Enum):
    BLACK = auto()
    WHITE = auto()


class PieceType(Enum):
    KING = auto()
    QUEEN = auto()
    BISHOP = auto()
    HORSE = auto()
    TOWER = auto()
    PEON = auto()


class Piece(ABC):
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    @abstractmethod
    def move(self):
        pass


class King(Piece):
    def __init__(self):
        super().__init__(PieceType.KING, Color.BLACK)

    def move(self):
        print(f'Peça: {self.nome.name}, Cor: {self.cor.name}')


class Queen(Piece):
    def __init__(self):
        super().__init__(PieceType.QUEEN, Color.BLACK)

    def move(self):
        print(f'Peça: {self.nome.name}, Cor: {self.cor.name}')


class Bishop(Piece):
    def __init__(self):
        super().__init__(PieceType.BISHOP, Color.BLACK)

    def move(self):
        print(f'Peça: {self.nome.name}, Cor: {self.cor.name}')


H = King()
H.move() 

S = Queen()
S.move()

D = Bishop()
D.move()
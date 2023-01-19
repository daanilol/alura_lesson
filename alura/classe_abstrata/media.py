from abc import ABC, abstractmethod

class Media(ABC):
    numeros = []

    @abstractmethod
    def calcula(self):
        pass
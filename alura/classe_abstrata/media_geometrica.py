from media import Media
from math import prod


class MediaGeometrica(Media):
    def __init__(self, numeros):
        self.numeros = numeros

    def calcula(self):
        return prod(self.numeros) ** (1/len(self.numeros))


class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print('{} - {} - {} min - {}'.format(self._nome, self.ano, self.duracao, self.likes))


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print('{} - {} - {} Temporadas - {}'.format(self._nome, self.ano, self.temporadas, self.likes))


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)
        


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2017, 3)
todo_mundo_em_panico = Filme('todo mundo em panico', 1999, 120)
demolidor = Serie('demolidor', 2017, 5)

vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
todo_mundo_em_panico.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, todo_mundo_em_panico]
playlist_fds = Playlist('fim de semana', filmes_e_series)

print('Tamanho da playlist: {}'.format(len(playlist_fds.listagem)))

print(demolidor in playlist_fds)

for programa in playlist_fds:
    programa.imprime()


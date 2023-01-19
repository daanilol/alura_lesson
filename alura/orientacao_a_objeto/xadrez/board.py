

class Board:
    def __init__(self):
        self.board = [[x for x in range(8)] for x in range(8)]
        beakpoint()
        return self.board
from tile import tile
from PuzzleBoard import PuzzleBoard
from queue import Queue
from copy import deepcopy


class Node:
    def __init__(self, BoardGame, parent=None, move=""):
        self.Board = BoardGame
        self.parent = parent
        self.depth = 0
        if parent is None:
            self.depth = 0
            self.moves = move
        else:
            self.depth = parent.depth+1
            self.moves = parent.moves + move
    
    def succ(self):
        succs = Queue()
        for m in self.Board.moves:
            p = deepcopy(self.Board)
            p.move(m)
            if p.zero is not self.Board.zero:
                succs.put(Node(p, self, m))
        return succs

    def __str__(self):
        return str(self.moves)
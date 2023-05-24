from PuzzleBoard import PuzzleBoard
from Node import Node
from queue import LifoQueue


class Search:
   def __init__(self, BoardA):
        self.start = Node(BoardA)
    
   def iterativeDeepening(self):
        self.depth = 0
        result = None
        while result == None:
            result = self.depthLimited(self.depth)
            self.depth +=1
            
        return result


   def depthLimited(self, depth):
        levels = LifoQueue()
        levels.put(self.start)
        while True:
            if levels.empty():
                return None
            actual = levels.get()
            if (actual.Board).checkPuzzle():
                return actual
            elif actual.depth is not depth:
                taker1 = actual.taker()
                while not taker1.empty():
                    levels.put(taker1.get())

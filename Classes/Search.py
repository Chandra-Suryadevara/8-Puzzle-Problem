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
        leaves = LifoQueue()
        leaves.put(self.start)
        while True:
            if leaves.empty():
                return None
            actual = leaves.get()
            if (actual.Board).checkPuzzle():
                return actual
            elif actual.depth is not depth:
                succ1 = actual.succ()
                while not succ1.empty():
                    leaves.put(succ1.get())

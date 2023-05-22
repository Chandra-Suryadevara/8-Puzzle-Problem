from PuzzleBoard import PuzzleBoard
from Search import Search

print("starting")
title = [1,2,3,4,5,0,6,7,8]
board = PuzzleBoard(title)
Search1 = Search(board)
print(Search1.iterativeDeepening())

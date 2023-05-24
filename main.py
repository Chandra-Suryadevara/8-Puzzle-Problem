from PuzzleBoard import PuzzleBoard
from Search import Search

print("starting")
input_string = input("Enter elements of the list separated by spaces or Enter DEFAULT to set list as 1,2,3,4,5,0,7,8,6 : ")
if(input_string != "DEFAULT") :
  title = list(map(int, input_string.split()))
else :
    title = [1,2,3,4,5,0,7,8,6]

board = PuzzleBoard(title)
Search1 = Search(board)
print(" ")
print("MOVES REQUIRED TO REACH GOAL STATE D[DOWN} U[UP] R[RIGHT] L[LEFT] : ", Search1.iterativeDeepening())

board.printBoard()
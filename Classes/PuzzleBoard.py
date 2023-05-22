from tile import tile

class PuzzleBoard:

    def __init__(self, tilesgiven):
       self.i = 0
       self.key1 = None
       self.key2 = None
       self.zero=(self.key1,self.key2)
       self.moves=['U','D','L','R']
       self.tiles = [[0 for _ in range(3)] for _ in range(3)]
       for x in range(3):
            for y in range(3):
                self.n=tile(tilesgiven[self.i]) 
                self.tiles[x][y] = self.n
                self.i += 1
                
    def printBoard(self):
     print(" ")
     for i in range(3):
        for j in range(3):
            if self.tiles[i][j].value() == 0:
                print("  ", end="")  # Print a blank space for the empty tile
            else:
                print(f"{self.tiles[i][j].value():2d}", end="")
            if j != 2:
                print(" | ", end="")  # Print vertical separators between tiles
        print()  # Move to the next line
        if i != 2:
            print("--------------")  # Print horizontal separator between rows

       
    
    def move(self,direction):
        
        
        for x in range(3):
             for y in range(3):
                 if (self.tiles[x][y]).value() == 0:
                     key1 = x
                     key2 = y
                     self.key1=key1
                     self.key2=key2
                     self.zero=(self.key1,self.key2)
        if self.key1 != None and self.key2 != None:

         if direction == 'R':
                self.temp = None
                if key2 == 2:
                    return 0
                else :
                    self.temp =self.tiles[key1][key2+1]
                    self.tiles[key1][key2+1]=self.tiles[key1][key2]
                    self.key2=key2+1
                    self.tiles[key1][key2]=self.temp
                    self.zero=(self.key1,self.key2)
  
         elif direction == 'L':
                self.temp = None
                if key2 == 0:
                    return 0
                else :
                    self.temp =self.tiles[key1][key2-1]
                    self.tiles[key1][key2-1]=self.tiles[key1][key2]
                    self.key2=key2-1
                    self.tiles[key1][key2]=self.temp
                    self.zero=(self.key1,self.key2)
         elif direction == 'U':
                self.temp = None
                if key1 == 0:
                    return 0
                else :
                    self.temp =self.tiles[key1-1][key2]
                    self.tiles[key1-1][key2]=self.tiles[key1][key2]
                    self.key1=key1-1
                    self.tiles[key1][key2]=self.temp
                    self.zero=(self.key1,self.key2)
         elif direction == 'D':
                self.temp = None
                if key1 == 2:
                    return 0
                else :
                    self.temp =self.tiles[key1+1][key2]
                    self.tiles[key1+1][key2]=self.tiles[key1][key2]
                    self.key1=key1+1
                    self.tiles[key1][key2]=self.temp
                    self.zero=(self.key1,self.key2)
         else: 
                print("Direction is wrong")
                return 0
        else:
            print("sorry")
            return 0

    def checkPuzzle(self):
      count=1
      for i in range(0,3):
          for j in range(0,3):
              if self.tiles[i][j].value()!=(count%(3*3)):
                  return False
              count+=1
      self.printBoard()
      return True


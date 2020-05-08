import sys

class Point():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    def printPoint(self):
        return "("+str(self.x)+", "+str(self.y)+")"

class Board():
    def __init__(self):
        self.NONE, self.X, self.O = 0, 1, 2
        self.game =[[0,0,0] for _ in range(3)]
        self.moves = Point(0, 0)
        for i in range(0, 3):
            for j in range(0, 3):
                self.game[i][j] = self.NONE
    def playerWon(self, player):
        if (self.game[0][0] == self.game[1][1] and self.game[0][0] == self.game[2][2] and self.game[0][0] == player) or (self.game[0][2] == self.game[1][1] and self.game[0][2] == self.game[2][0] and self.game[0][2] == player):
            return True
        for i in range(3):
            if (self.game[i][0] == self.game[i][1] and self.game[i][0] == self.game[i][2] and self.game[i][0] == player) or (self.game[0][i] == self.game[1][i] and self.game[0][i] == self.game[2][i] and self.game[0][i] == player):
                return True
        return False
    def cells(self):
        availabeCell = []
        for i in range(3):
            for j in range(3):
                if self.game[i][j] == self.NONE:
                    availabeCell.append(Point(i, j))
        return availabeCell
    def Over(self):
        cell = self.cells()
        return self.playerWon(self.X) or self.playerWon(self.O) or len(cell) == 0
    def move(self, Point, player):
        if self.game[Point.x][Point.y] != self.NONE:
            return False
        self.game[Point.x][Point.y] = player
        return True 
    def printBoard(self):
        print()
        for i in range(3):
            print("\t", end=" ")
            for j in range(0,3):
                player = " "
                if self.game[i][j] == self.X:
                    print ("X", end=" ") 
                elif self.game[i][j] == self.O:
                    print ("O", end=" ") 
                else:
                    print (player, end=" ")
                if j!=2:
                    print (" | ", end=" ")
            print()
            if i!=2:
                print ("\t----+-----+----")
        print()
    def minimax(self, depth, turn):
        if self.playerWon(self.X):
            return 1
        if self.playerWon(self.O) == True:
            return -1
        cell = self.cells()
        if(len(cell)==0):
            return 0
        maxim = -int(sys.maxsize)
        minim = int(sys.maxsize)
        for i in range(len(cell)):
            point = cell[i]
            if turn == self.X:
                self.move(point, self.X)
                currentScore = self.minimax(depth+1, self.O)
                maxim = max(currentScore, maxim)
                if currentScore >= 0:
                    if depth == 0 or len(cell)==0:
                        self.moves = point
                if currentScore == 1:
                    self.game[point.x][point.y] = self.NONE
                    break
            if turn == self.O:
                self.move(point, self.O)
                currentScore = self.minimax(depth+1, self.X)
                minim = min(currentScore, minim)
                if minim == -1:
                    self.game[point.x][point.y] =  self.NONE
                    break
            self.game[point.x][point.y] = self.NONE
        if turn == self.X:
            return maxim
        return minim

class TicTacToe():
    def coordinates(self,x):
        if x==1:
            return 0, 0
        elif x==2:
            return 0, 1
        elif x==3:
            return 0, 2
        elif x==4:
            return 1, 0
        elif x==5:
            return 1, 1
        elif x==6:
            return 1, 2
        elif x==7:
            return 2, 0
        elif x==8:
            return 2, 1
        elif x==9:
            return 2, 2
        else:
            return None, None
    def game(self):
        tic = Board()
        tic.printBoard()
        while not tic.Over():
            moveOk = True
            while(True):
                if not moveOk:
                    print("Cell Not Empty.\n")
                move = int(input("Your Move--> "))
                x, y = self.coordinates(move)
                if x==None or y==None:
                    print("Invalid Cell Number.\n")
                    continue
                user = Point(x, y)
                moveOk = tic.move(user, tic.O)
                if moveOk:
                    break
            tic.printBoard()
            if tic.Over():
                break
            tic.minimax(0, tic.X)
            tic.move(tic.moves, tic.X)
            tic.printBoard()
        if tic.playerWon(tic.X):
            print("Result--> Computer won the game.")
        elif tic.playerWon(tic.O):
            print("Result--> You won the game.")
        else:
            print("Result--> Draw.")

Obj = TicTacToe()
Obj.game()
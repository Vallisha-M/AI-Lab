GRID_SIZE = 3
class TicTacToe:
    def __init__(self, firstChance :str):
        self.grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.players = ['x', 'o']
        self.player = 0 if firstChance.lower()=='x' else 1
    def isVacant(self, move:tuple)->bool:
        if self.grid[move[0]][move[1]]==' ':
            return True
        return False
    def isFull(self):
        for i in self.grid:
            for j in i:
                if j==' ':
                    return False
        return True
    def isDraw(self):
        return (not self.won()) and self.isFull()

    def getSize(self):
        return GRID_SIZE
    def won(self)->bool:
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] ==self.players[self.player]:
                return True
        for i in range(3):
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] ==self.players[self.player]:
                return True
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] ==self.players[self.player]:
            return True
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] ==self.players[self.player]:
            return True
        return False
            

    def turn(self):
        return self.player+1
    def agent_step(self, move:tuple)->int:
        if self.isVacant(move):
            self.grid[move[0]][move[1]]=self.players[self.player]
            if self.won():
                return self.player
            
            return -1
        else:
            return -2
    def printGrid(self):
        print('-'*7)
        print('|'+self.grid[0][0]+'|'+self.grid[0][1]+'|'+self.grid[0][2]+'|')
        print('-'*7)
        print('|'+self.grid[1][0]+'|'+self.grid[1][1]+'|'+self.grid[1][2]+'|')
        print('-'*7)
        print('|'+self.grid[2][0]+'|'+self.grid[2][1]+'|'+self.grid[2][2]+'|')
        print('-'*7)

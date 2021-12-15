import random
from copy import deepcopy
class Agent:
    def __init__(self):
        pass
    def select_random(self,array:list)->int:
        return array[random.randint(0, len(array)-1)]
    def won(self,grid:list, player:str)->bool:
        for i in range(3):
            if  grid[i][0] == grid[i][1] ==  grid[i][2] == player:
                    return True
        for i in range(3):
            if  grid[0][i] ==  grid[1][i] ==  grid[2][i] == player:
                return True
        if  grid[0][0] ==  grid[1][1] ==  grid[2][2] == player:
            return True
        if  grid[0][2] ==  grid[1][1] ==  grid[2][0] == player:
            return True
        return False
    def select_action(self,grid:list, mine:str, next:str)->tuple:
        grid_copy = deepcopy(grid)
        available_moves=[]
        for i in range(3):
            for j in range(3):
                if grid[i][j]==' ':
                    available_moves.append(i*3+j+1)
        corners=[]
        move=0
        mid_place=[]
        for j in [mine, next]:
            for i in available_moves:
                if i<=3:
                    row=0
                elif i<=6:
                    row=1
                else:
                    row=2
                column=i-row*3-1
            
                grid_copy = deepcopy(grid)
                
                grid_copy[row][column]=j

                if self.won(grid_copy, j):
                    return (row, column)
   
        for i in available_moves:
            if i==1 or i==3 or i==7 or i==9:
                corners.append(i)
            elif i==2 or i==4 or i==6 or i==8:
                mid_place.append(i)
        if(len(corners)>0):
            move = self.select_random(corners)
        elif(5 in available_moves):
            move=5
        elif(len(mid_place)>0):
            move = self.select_random(mid_place)

        if move<=3:
            r=0
        elif move<=6:
            r=1
        else:
            r=2

        c=move-r*3-1
        return (r, c)

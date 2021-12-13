import os
import time
from TicTacToe import TicTacToe
from Agent import Agent
first_player = input('Enter x to play first : ')
agent = Agent()
game = TicTacToe(first_player)
won = False
while(not won):
    os.system('clear')
    current_player = game.player
    game.printGrid()
    size = game.getSize()
    if(current_player==1):
        print("AI's turn")
        time.sleep(1)
    else:
        print('Player'+str(current_player)+"'s turn")
        print('Enter row and column;')
    while True:
        if current_player==0:
            r, c = map(str, input().split())
        else:
            (r, c) = agent.select_action(game.grid, game.players[game.player],game.players[(game.player+1)%2])
            r=str(r)
            c=str(c)
        if (not r.isdigit() or not c.isdigit()):
            print('Invalid Selection')
        else:
            r,c = int(r), int(c)
            if(r<size and c<size) and (r>-1 and c>-1):
                result = game.agent_step((r, c))
                if result==-2:
                    print("Not Vacant")
                if result>-1:
                    if(current_player==0):
                        print('You won!')
                    else:
                        print("AI won")
                    game.printGrid()
                    won = True
                    break
                if game.isDraw():
                    os.system('clear')
                    game.printGrid()
                    print('Draw!')
                    won = True
                    break
                    
                if result==-1:
                    game.player = (game.player+1)%2
                    break
            else:
                print('Invalid Selection')   
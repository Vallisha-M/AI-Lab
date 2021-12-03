import os
from TicTacToe import TicTacToe

first_player = input('Enter symbol for player : ')
game = TicTacToe(first_player)
won = False
while(not won):
    os.system('clear')
    current_player = game.player
    game.printGrid()
    size = game.getSize()
    print('Player'+str(current_player)+"'s turn")
    print('Enter row and column;')
    while True:
        r, c = map(str, input().split())
        if (not r.isdigit() or not c.isdigit()):
            print('Invalid Selection')
        else:
            r,c = int(r), int(c)
            if(r<size and c<size) and (r>-1 and c>-1):
                result = game.agent_step((r, c))
                if result==-2:
                    print("Not Vacant")
                if result>-1:
                    print('Player', str(current_player), ' has won!')
                    won = True
                    break
                if game.isDraw():
                    print('Draw!')
                    won = True
                    break
                    
                if result==-1:
                    game.player = (game.player+1)%2
                    break
            else:
                print('Invalid Selection')   
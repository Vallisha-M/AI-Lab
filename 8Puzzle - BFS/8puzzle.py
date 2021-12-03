from copy import deepcopy
def check(state, target):
    for i in range(3):
        for j in range(3):
            if state[i][j]!=target[i][j]:
                return False
    return True
def getIndex(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]=='-1':
                return (i, j)
    return (-1, -1)

def display(state):
    print('-'*7)
    print('|'+state[0][0]+'|'+state[0][1]+'|'+state[0][2]+'|')
    print('-'*7)
    print('|'+state[1][0]+'|'+state[1][1]+'|'+state[1][2]+'|')
    print('-'*7)
    print('|'+state[2][0]+'|'+state[2][1]+'|'+state[2][2]+'|')
    print('-'*7)
def bfs(state, target):
    queue = [state]
    while len(queue)>0:
        current_state = queue.pop(0)
        print('Current State')
        display(current_state)
        index = getIndex(current_state)
        if check(current_state, target):
            print("Solution found")
            exit(0)
        if index[0]==-1:
            print("Error")
            exit(-1)
        if index[1]>0: #left
            current_state_copy = deepcopy(current_state)
            current_state_copy[index[0]][index[1]-1], current_state_copy[index[0]][index[1]] = current_state_copy[index[0]][index[1]-1], current_state_copy[index[0]][index[1]] 
            if check(current_state_copy, target):
                print("Solution")
                display(current_state_copy)
                print("Solution found")
                exit(0)
            else:
                queue.append(current_state_copy)
        if index[1]<2: #right
            current_state_copy = deepcopy(current_state)
            current_state_copy[index[0]][index[1]+1], current_state_copy[index[0]][index[1]] = current_state_copy[index[0]][index[1]+1], current_state_copy[index[0]][index[1]] 
            if check(current_state_copy, target):
                print("Solution")
                display(current_state_copy)
                print("Solution found")
                exit(0)
            else:
                queue.append(current_state_copy)
        if index[0]>0: #up
            current_state_copy = deepcopy(current_state)
            current_state_copy[index[0]][index[1]], current_state_copy[index[0]-1][index[1]] = current_state_copy[index[0]-1][index[1]], current_state_copy[index[0]][index[1]] 
            if check(current_state_copy, target):
                print("Solution")
                display(current_state_copy)
                print("Solution found")
                exit(0)
            else:
                queue.append(current_state_copy)

        if index[0]<2: #down
            current_state_copy = deepcopy(current_state)
            current_state_copy[index[0]][index[1]], current_state_copy[index[0]+1][index[1]] = current_state_copy[index[0]+1][index[1]], current_state_copy[index[0]][index[1]] 
            if check(current_state_copy, target):
                print("Solution")
                display(current_state_copy)
                print("Solution found")
                exit(0)
            else:
                queue.append(current_state_copy)
print("Enter the start state;")
state = [[i for i in input().split()] for j in range(3)]
print("Enter target state;")
target = [[i for i in input().split()] for j in range(3)]
bfs(state, target)
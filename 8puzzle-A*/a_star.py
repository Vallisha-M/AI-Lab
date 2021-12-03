from copy import deepcopy
from queue import PriorityQueue

def check(state, target):
    for i in range(3):
        for j in range(3):
            if state[i][j] != target[i][j]:
                return False
    return True

def get_loc(state, tile):
    for i in range(0, 3):
        for j in range(0, 3):
            if(state[i][j]==tile):
                return (i, j)

def getHeuristic(state, target):
    result=0
    for i in range(0, 3):
        for j in range(0,3):
            if(state[i][j]!='-1'):
                target_loc = get_loc(target, state[i][j])
                result += abs(i-target_loc[0])+abs(j-target_loc[1])
    return result

def getIndex(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == '-1':
                return [i, j]
    return -1

def display(state):
    for i in state:
        for j in i:
            print(j, end = " ")
        print()

def a_star(state, target):
    count = 0
    queue = PriorityQueue()
    queue.put((getHeuristic(state, target), [state, 0]))
    print("Current State")
    display(state)
    if check(state, target):
        print("Solution found")
        exit(0)

    while queue.qsize() > 0:
        state_aggregate = queue.get()[1]
        level = state_aggregate[1]
        state = state_aggregate[0]
        index = getIndex(state)
        if index == -1:
            print("Error")
            print(state)
            exit(0)

        if index[1]-1 >= 0:          # Left
            state1 = deepcopy(state)
            state1[index[0]][index[1]-1], state1[index[0]][index[1]] = state1[index[0]][index[1]], state1[index[0]][index[1]-1]
            print("Current State")
            display(state1)
            if check(state1, target):
                print(f"Solution found in {count} steps")
                exit(0)
            else:
                count += 1
                queue.put((level+getHeuristic(state1, target)+1,[state1, level+1]))

        if index[1]+1 < 3:          # Right
            state1 = deepcopy(state)
            state1[index[0]][index[1]+1], state1[index[0]][index[1]] = state1[index[0]][index[1]], state1[index[0]][index[1]+1]
            print("Current State")
            display(state1)
            if check(state1, target):
                print(f"Solution found in {count} steps")
                exit(0)
            else:
                count += 1
                queue.put((level+getHeuristic(state1, target)+1,[state1, level+1]))

        if index[0]-1 >= 0:         # Up
            state1 = deepcopy(state)
            state1[index[0]-1][index[1]], state1[index[0]][index[1]] = state1[index[0]][index[1]], state1[index[0]-1][index[1]]
            print("Current State")
            display(state1)
            if check(state1, target):
                print(f"Solution found in {count} steps")
                exit(0)
            else:
                count += 1
                queue.put(((level+getHeuristic(state1, target)+1,[state1, level+1])))


        if index[0]+1 < 3:         # Down
            state1 = deepcopy(state)
            state1[index[0]+1][index[1]], state1[index[0]][index[1]] = state1[index[0]][index[1]], state1[index[0]+1][index[1]]
            print("Current State")
            display(state1)
            if check(state1, target):
                print(f"Solution found in {count} steps")
                exit(0)
            else:
                count += 1
                queue.put((level+getHeuristic(state1, target)+1,[state1, level+1]))


print("Enter the start state")
state = [[i for i in input().split()] for j in range(3)]

print("Enter the target state")
target = [[i for i in input().split()] for j in range(3)]

a_star(state, target)
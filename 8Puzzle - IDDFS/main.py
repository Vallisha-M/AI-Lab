from copy import deepcopy

count = 0

def check(state, target):
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] != target[i][j]:
                return False
    return True

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

def ids(state, target, max_limit):
    for limit in range(max_limit+1):
        print(f"Level = {limit}")
        dls(state, target, limit)
    print("No solution found")

def dls(state, target, limit):
    global count
    stack = [[state, limit]]
    print("Current State")
    display(state)
    if check(state, target):
        print("Solution found")
        exit(0)

    while len(stack) > 0:
        x = stack.pop(-1)
        state = x[0]
        level = x[1]
        index = getIndex(state)
        if index == -1:
            print("Error")
            print(state)
            exit(0)
        if index[1]-1 >= 0:          # Left
            state1 = deepcopy(state)
            state1[index[0]][index[1]-1], state1[index[0]][index[1]] = state1[index[0]][index[1]], state1[index[0]][index[1]-1]
            count += 1
            print("Current State")
            display(state1)
            if check(state1, target):
                print(f"Solution found in {count} steps")
                exit(0)
            else:
                if level > 1:
                    stack.append([state1, level-1])

        if index[1]+1 < 3:          # Right
            state1 = deepcopy(state)
            state1[index[0]][index[1]+1], state1[index[0]][index[1]] = state1[index[0]][index[1]], state1[index[0]][index[1]+1]
            count += 1
            print("Current State")
            display(state1)
            if check(state1, target):
                print(f"Solution found in {count} steps")
                exit(0)
            else:
                if level > 1:
                    stack.append([state1, level-1])

        if index[0]-1 >= 0:         # Up
            state1 = deepcopy(state)
            state1[index[0]-1][index[1]], state1[index[0]][index[1]] = state1[index[0]][index[1]], state1[index[0]-1][index[1]]
            count += 1
            print("Current State")
            display(state1)
            if check(state1, target):
                print(f"Solution found in {count} steps")
                exit(0)
            else:
                if level > 1:
                    stack.append([state1, level-1])

        if index[0]+1 < 3:         # Down
            state1 = deepcopy(state)
            state1[index[0]+1][index[1]], state1[index[0]][index[1]] = state1[index[0]][index[1]], state1[index[0]+1][index[1]]
            count += 1
            print("Current State")
            display(state1)
            if check(state1, target):
                print(f"Solution found in {count} steps")
                exit(0)
            else:
                if level > 1:
                    stack.append([state1, level-1])

print("Enter the start state")
state = [[i for i in input().split()] for j in range(3)]

print("Enter the target state")
target = [[i for i in input().split()] for j in range(3)]

max_limit = int(input("Enter the maximum limit: "))
ids(state, target, max_limit)
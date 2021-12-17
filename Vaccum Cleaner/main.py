def clean(floor,row,col):
    i,j,m,n = row,col,len(floor),len(floor[0])
    goRight = goDown = True
    cleaned = [not any(f) for f in floor]
    while not all(cleaned):
        while any(floor[i]):
            printfloor(floor,i,j)
            if floor[i][j]:
                floor[i][j]=0
                printfloor(floor,i,j)
            if not any(floor[i]):
                cleaned[i]=True
                break
            if j == n-1:
                j -= 1
                goRight=False
            elif j == 0:
                j += 1
                goRight=True
            else:
                j += 1 if goRight else -1
        if all(cleaned):
            break
        if i == m-1:
            i -= 1
            goDown=False
        elif i == 0:
            i += 1
            goDown=True
        else:
            i += 1 if goDown else -1
        if cleaned[i]:
            printfloor(floor,i,j)

def printfloor(floor,row,col):
    for i in range(len(floor)):
        for j in range(len(floor[i])):
            if i == row and j == col:
                print(f" *{floor[i][j]}* ", end = '')
            else:
                print(f"  {floor[i][j]}  ", end = '')
        print()
    print()

floor = [[1, 0, 0, 1, 0],
         [0, 1, 0, 1, 1],
         [1, 0, 1, 0 ,0],
         [1, 0, 0, 1, 0],
         [1, 0, 0, 1, 1]]

clean(floor, 0, 0)
print("Cleaned")

for i in range(int(input())):
    row  = int(input())
    col  = int(input())
    pizzaMap = [] # The char map

    for j in range(row):
        pizzaMap.append(input())

    possPaths = [(0,0,1)] # tuples of (x, y, intersections)
    traversed = []

    # symbol being (0,0) mapped to the points you can add to it
    moves = {
             '+':[(1,0),(-1,0),(0,1),(0,-1)], # N S E W
             '|':[(0,1),(0,-1)], # N S
             '-':[(1,0),(-1,0)]  # E W
            }

    while True:
        if len(possPaths) == 0: # if Im blocked and can't traverse
            print (-1)
            break

        x,y,intersections = possPaths.pop(0)
        if (x == -1 or x == col) or (y == -1 or y == row):
            continue

        if pizzaMap[y][x] == '*':
            continue

        if (x,y) in traversed:
            continue

        if (x,y) == (col-1,row-1): # we are at the south-east
            # print (intersections)
            break


        traversed.append((x,y))
        symbol = pizzaMap[y][x]

        for (dx,dy) in moves[symbol]: # adding the possibilities
            possPaths.append((x+dx, y+dy, intersections+1))
        print (possPaths)
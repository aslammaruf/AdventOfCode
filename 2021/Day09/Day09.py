import numpy as np
# Part 1

def SmokeBasin( data ):
    answer = []

    for y, row in enumerate( data ):
        for x, col in enumerate( row ):
            up = data[y - 1][x] if y - 1 >= 0 else 9
            down = data[y + 1][x] if y + 1 < len(data) else 9
            right = data[y][x + 1] if x + 1 < len(row) else 9
            left = data[y][x - 1] if x - 1 >= 0 else 9
            if ( up > col and down > col and left > col and right > col ):
                answer.append(col)
                lowpoints.append( (x, y) )

    return sum(answer) + (1 * len(answer))

# Part 2

def SmokeBasinP2( ):
    sizes = []

    for basin in lowpoints:
        sizes.append(len(getBasinSize( basin[0], basin[1], [] )))

    return np.array( sorted(sizes)[-3:] ).prod()

def getBasinSize( x, y, BasinSize):
    up = data[y - 1][x] if y - 1 >= 0 else 9
    down = data[y + 1][x] if y + 1 < len(data) else 9
    right = data[y][x + 1] if x + 1 < len(data[0]) else 9
    left = data[y][x - 1] if x - 1 >= 0 else 9
    BasinSize.append( (x, y) )

    if up != 9 and (x, y - 1) not in BasinSize:
        getBasinSize( x, y - 1, BasinSize)
    if down != 9 and (x, y + 1) not in BasinSize:
        getBasinSize( x, y + 1, BasinSize)
    if left != 9 and (x - 1, y) not in BasinSize:
        getBasinSize( x - 1, y, BasinSize)
    if right != 9 and (x + 1, y) not in BasinSize:
        getBasinSize( x + 1, y, BasinSize)
    
    return BasinSize



lowpoints = []

with open('Day09/input.txt') as f:
    data = np.array([ list(line.strip()) for line in f]).astype(int)

p1Answer = SmokeBasin( data )
p2Answer = SmokeBasinP2()

print()
print(f'Part 1: : {p1Answer}')
print(f'Part 2: : {p2Answer}')
print()
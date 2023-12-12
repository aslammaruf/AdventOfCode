import numpy as np
# Part 1

def PassagePathing( data ):
    x = np.where( data == 'start' )
    paths = []
    currPath = []
    print( '\n ')

    loc = 'start'
    y = []

    while y != False:
        loc = getPath( loc )
        if loc == False: y = False

    return 0

def getPath( loc ):
    connectPaths = [ nextLoc for nextLoc in data if nextLoc[0] == loc ]
    if connectPaths == []:
        return False
    else:
        print( connectPaths[0] )
        return connectPaths[0][1]

# Part 2

def PassagePathingP2( data ):

    return 0


with open('Day12/test.txt') as f:
    data = np.array([ line.strip().split('-') for line in f])

print( data )
p1Answer = PassagePathing( data )
p2Answer = PassagePathingP2( data )

print()
print(f'Part 1: : {p1Answer}')
print(f'Part 2: : {p2Answer}')
print()
import numpy as np

# Part 1

def TreacheryOfWhales( data ):
    lfr = np.inf
    for pos in range(min(data), max(data) + 1):
        posdiff = np.absolute(data - pos)
        if np.sum(posdiff) > lfr:
            return lfr
        lfr = np.sum(posdiff)
    return 0

# Part 2

def TreacheryOfWhalesP2( data ):
    lfr = np.inf
    for pos in range(min(data), max(data) + 1):
        n = np.absolute(data - pos)
        fr = ( n * (n + 1) ) / 2
        if np.sum(fr) > lfr:
            return int(lfr)
        lfr = np.sum(fr)
    return 0


with open('Day07/input.txt') as f:
    data = np.array( list(map( int, [ line.split(',') for line in f][0] ) ) )

p1Answer = TreacheryOfWhales( data )
p2Answer = TreacheryOfWhalesP2( data )

print()
print(f'Part 1: : {p1Answer}')
print(f'Part 2: : {p2Answer}')
print()
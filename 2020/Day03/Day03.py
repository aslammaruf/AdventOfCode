import math

def TobogganTrajectory( arr, rowIncrement, colIncrement ):
    treeEncounter = row = col = 0
    rowBound = len( arr ) 
    colBound = len( arr[0] )

    while row < rowBound:
        if arr[ row ][ col ] == "#":
            treeEncounter += 1

        row += rowIncrement
        col += colIncrement 

        if col >= colBound:
            col = col - colBound

    return treeEncounter

with open('Day03/input.txt') as f:
    arr = [ list(line.strip()) for line in f ]

slopeList = [[1,1], [1,3], [1,5], [1,7], [2,1]]

print( f'Part 1 result : { TobogganTrajectory( arr , 1 , 3 ) }') 
print( f'Part 2 result : { math.prod([ TobogganTrajectory( arr, down , right ) for down, right in slopeList ]) }')

print( [ TobogganTrajectory( arr, down , right ) for down, right in slopeList ] )
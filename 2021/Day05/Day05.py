import numpy as np

# Part 1

def HydrothermalVenture( arr, dim, HorandVert):
    if HorandVert:
        arr = [ line for line in arr if line[0] == line[2] or line[1] == line[3] ]

    x = np.zeros((dim, dim))

    for line in arr:
        points = []
        line = list( map( int, line ))
        if line[0] == line[2] or line[1] == line[3]:
            for i in range(abs(line[0] - line[2]) + 1):
                for j in range( abs(line[1] - line[3]) + 1):
                    points += [ ( i + min(line[0], line[2]) , j + min(line[1], line[3]) ) ]
        else : 
            a = 1 if (line[0] - line[2]) < 0 else -1
            b = 1 if (line[1] - line[3]) < 0 else -1
            for i in range(abs(line[0] - line[2]) + 1):
                    points += [ ( line[0] + (i * a) , line[1] + (i * b) ) ]

        for point in points:
            x[ point[1] ][ point[0] ] += 1

    return np.sum(x > 1)

with open('Day05/input.txt') as f:
    arr = [ line.replace(' -> ',',').strip().split(',') for line in f]

 # arr[ line ][ x1 ][ y1 ][ x2 ][ y2 ]
dim = 1000
p1Answer = HydrothermalVenture( arr , dim, True )
p2Answer = HydrothermalVenture( arr , dim, False)

print()
print(f'Part 1: 2 Lines Overlap : {p1Answer}')
print(f'Part 2: Last Winning Bingo : {p2Answer}')
print()

#Resulting double points only vert/hor: 6397
#Resulting double points vert/hor/diag: 22335
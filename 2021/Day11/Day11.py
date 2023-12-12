import numpy as np
# Part 1

def DumboOctopus( data, maxStep ):
    numFlashes = 0

    for _ in range(0, maxStep):
        data += 1
        z = np.array(np.where(data >  9)).T

        i = 0
        while i < len(z):
            point = z[i]
            for pos in posArr:
                if point[0] + pos[1] >= 0 and point[0] + pos[1] < 10 and point[1] + pos[0] >= 0 and point[1] + pos[0] < 10 :
                    data[ point[0] + pos[1] ][ point[1] + pos[0] ] += 1
                    y = [point[0] + pos[1], point[1] + pos[0]]
                    if data[ point[0] + pos[1] ][ point[1] + pos[0] ] > 9: 
                        if y not in z.tolist():
                            newRow = [point[0] + pos[1], point[1] + pos[0]]
                            z = np.vstack([z , newRow])
            i += 1

        numFlashes += np.sum( data > 9 )
        data[ data > 9 ] = 0

    return numFlashes

# Part 2

def DumboOctopusP2( data ):
    step = 0
    sync = False

    while sync != True:
        data += 1
        z = np.array(np.where(data >  9)).T

        i = 0
        while i < len(z):
            point = z[i]
            for pos in posArr:
                if point[0] + pos[1] >= 0 and point[0] + pos[1] < 10 and point[1] + pos[0] >= 0 and point[1] + pos[0] < 10 :
                    data[ point[0] + pos[1] ][ point[1] + pos[0] ] += 1
                    y = [point[0] + pos[1], point[1] + pos[0]]
                    if data[ point[0] + pos[1] ][ point[1] + pos[0] ] > 9: 
                        if y not in z.tolist():
                            newRow = [point[0] + pos[1], point[1] + pos[0]]
                            z = np.vstack([z , newRow])
            i += 1

        sync = True if np.sum( data > 9 ) == 100 else False
        data[ data > 9 ] = 0
        step += 1

    return step + 100


with open('Day11/input.txt') as f:
    data = np.array([ list(line.strip()) for line in f]).astype(int)

posArr = [ (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1) ]

p1Answer = DumboOctopus( data , 100)
p2Answer = DumboOctopusP2( data )

print()
print(f'Part 1: : {p1Answer}')
print(f'Part 2: : {p2Answer}')
print()
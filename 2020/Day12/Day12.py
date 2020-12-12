def RainRisk():
    x = y = 0
    shipFacing = 90

    x = sum( [ value for direction , value in arr if direction == "N"] ) - sum( [ value for direction , value in arr if direction == "S"] )
    y = sum( [ value for direction , value in arr if direction == "E"] ) - sum( [ value for direction , value in arr if direction == "W"] )

    LRF = [ ( direction , value ) for direction , value in arr if direction == "R" or direction == "L" or direction == "F" ]
    
    for direction , value in LRF:
        if direction == "L":
            shipFacing = ( shipFacing - value ) % 360
        elif direction == "R":
            shipFacing = ( shipFacing + value ) % 360
        elif direction == "F":
            if shipFacing == 0:
                x += value
            elif shipFacing == 180:
                x -= value
            elif shipFacing == 90:
                y += value
            elif shipFacing == 270:
                y -= value

    return abs(x) + abs(y)

def RainRiskP2():
    # loc - location of ship , wp - location of waypoint, rot - Rotation Matrix of cartesian coordinates for 90, 180, 270
    loc = [ 0 , 0 ]
    wp = [ 1 , 10 ]
    rot = [ (0, -1, 1, 0) , (-1, 0, 0, -1) , (0, 1, -1, 0)] 

    for direction,  value in arr:
        
        if direction == "N":
            wp[0] += value
        elif direction == "S":
            wp[0] -= value
        elif direction == "E":
            wp[1] += value
        elif direction == "W":
            wp[1] -= value

        elif direction == "F":
            loc = [ loc[0] + ( value * wp[0] ) , loc[1] + ( value * wp[1] ) ]

        elif direction == "R" or direction == "L":
            # Calculates the degrees going counter clockwise
            # Converts degrees into rot index
            # Apply rotation matrix to waypoint(wp)
            deg = 360 - ( ( value if direction == "R" else - value ) % 360 ) 
            ri = int( deg / 90 ) - 1 
            wp = [ (wp[1] * rot[ri][2] + wp[0] * rot[ri][3]) , (wp[1] * rot[ri][0] + wp[0] * rot[ri][1]) ]

    return abs( loc[0] ) + abs( loc[1] )

# Main

filename = "Day12/input.txt"
arr = [ (line[:1] , int(line[1:]) ) for line in open( filename ).read().split("\n") ]

print( f'Part 1 answer : {RainRisk()}')
print( f'Part 2 answer : {RainRiskP2()}')
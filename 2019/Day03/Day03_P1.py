import math

def wireMovement( pos, mov ):
    w_dir = mov[0:1] # Creating substring to get Direction and Distance
    w_dis = mov[1::]
    if w_dir == "U":
        pos[1] += int(w_dis)
    elif w_dir == "R":
        pos[0] += int(w_dis)
    elif w_dir == "D":
        pos[1] -= int(w_dis)
    elif w_dir == "L":
        pos[0] -= int(w_dis)
    return( pos )

def CheckIntersection( w1Old, w1New, w2Old, w2New, IntersectionPoints ):
    # Check if lines are going oppersite directions
    # Check if lines interset
    if w1Old[0] == w1New[0] and w2Old[1] == w2New[1]:
        x = w1Old[0]
        y = w2Old[1]
        if (w1Old[1] < y and y < w1New[1]) or (w1New[1] < y and y < w1Old[1]):
            if (w2Old[0] < x and x < w2New[0]) or (w2New[0] < x and x < w2Old[0]):
                return [x,y]
    elif w2Old[0] == w2New[0] and w1Old[1] == w1New[1]:
        x = w2Old[0]
        y = w1Old[1]
        if (w2Old[1] < y and y < w2New[1]) or (w2New[1] < y and y < w2Old[1]):
            if (w1Old[0] < x and x < w1New[0]) or (w1New[0] < x and x < w1Old[0]):
                return [x,y]
    else:
        return None

def ManhattanDistance( coord, arrayPos, closestPoint ):
    dis = math.fabs(coord[0]) + math.fabs(coord[1])
    if dis < closestPoint:
        closestPoint = dis
    elif closestPoint == 0:
        closestPoint = dis
    return closestPoint

f = open("Day03/input.txt", "r")

w1 = f.readline()
w1_arr = w1.split(",")
w1_pos = [0,0]

w2 = f.readline()
w2_arr = w2.split(",")

IntersectionPoints = [None]

for Wire1 in range( len(w1_arr) ):
    w1_oldpos = w1_pos[:] # Prevents referencing w1_pos
    w1_pos = wireMovement( w1_pos, w1_arr[Wire1])
    w2_pos = [0,0]
    for Wire2 in range( len(w2_arr) ):
        w2_oldpos = w2_pos[:]
        w2_pos = wireMovement( w2_pos, w2_arr[Wire2])
        check = CheckIntersection( w1_oldpos, w1_pos, w2_oldpos, w2_pos, IntersectionPoints)
        if check != None:
            IntersectionPoints.append(check)

closestPoint = 0
for counter in range( 1, len(IntersectionPoints)):
    closestPoint = ManhattanDistance( IntersectionPoints[counter], counter, closestPoint)

print("Intersection Point : ", IntersectionPoints)
print("Closest Point : ", closestPoint)


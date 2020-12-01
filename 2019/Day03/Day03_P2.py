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

def CheckIfIntersection( w1Old, w1New, w2Old, w2New ):
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

def FewestSteps( point, w1_dis, w1_pos, w2_dis, w2_pos, fewestSteps ):
    disTointersection = math.fabs(point[0] - w1_pos[0]) + math.fabs(point[0] - w2_pos[0]) + math.fabs(point[1] - w1_pos[1]) + math.fabs(point[1] - w2_pos[1])
    dis = w1_dis + w2_dis + disTointersection
    if dis < fewestSteps:
        fewestSteps = dis
    elif fewestSteps == 0:
        fewestSteps = dis
    return fewestSteps

f = open("Day03/input.txt", "r")

w1 = f.readline()
w1_arr = w1.split(",")

w2 = f.readline()
w2_arr = w2.split(",")

w1_pos = [0,0]
w1_dis = 0
IntersectionPoints = [None]
CombinedSteps = 0

for Wire1 in range( len(w1_arr) ):
    w1_oldpos = w1_pos[:] # Prevents referencing w1_pos
    w1_pos = wireMovement( w1_pos, w1_arr[Wire1])
    w2_pos = [0,0]
    w2_dis = 0
    for Wire2 in range( len(w2_arr) ):
        w2_oldpos = w2_pos[:]
        w2_pos = wireMovement( w2_pos, w2_arr[Wire2])
        check = CheckIfIntersection( w1_oldpos, w1_pos, w2_oldpos, w2_pos)
        if check != None:
            CombinedSteps = FewestSteps( check, w1_dis, w1_oldpos, w2_dis, w2_oldpos, CombinedSteps)
            IntersectionPoints.append(check)
        w2_dis += int(w2_arr[Wire2][1::])
    w1_dis += int(w1_arr[Wire1][1::])

print("Intersection Point : ", IntersectionPoints)
print("Fewest Combined Steps : ", CombinedSteps)


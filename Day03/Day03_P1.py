import math

def wireMovement( pos, mov ):
    w_dir = mov[0:1] # Creating substring to get Direction and Distance
    w_dis = mov[1::]

    if w_dir == "U":
        pos[0] += int(w_dis)
    elif w_dir == "R":
        pos[1] += int(w_dis)
    elif w_dir == "D":
        pos[0] -= int(w_dis)
    elif w_dir == "L":
        pos[1] -= int(w_dis)

    return( pos )

def CheckIntersection( w1Old, w1New, w2Old, w2New ):
    if w1Old[0] < w1New [0]:
        xRange = [ w1Old[0], w1New[0] ]
    else:
        xRange = [ w1New[0], w1Old[0] ]

    if w1Old[1] < w1New [1]:
        yRange = [ w1Old[1], w1New[1] ]
    else:
        yRange = [ w1New[1], w1Old[1] ]

    if w2Old[0] < w2New [0]:
        w2_xRange = [ w2Old[0], w2New[0] ]
    else:
        w2_xRange = [ w2New[0], w2Old[0] ]

    if w2Old[1] < w2New [1]:
        w2_yRange = [ w2Old[1], w2New[1] ]
    else:
        w2_yRange = [ w2New[1], w2Old[1] ]

    print(w2_xRange, w2_yRange)
    # Check x coord
    if w2New[0] > xRange[0] and w2New[0] < xRange[1]:
        if yRange[0] < w2Old[1] and yRange[0] > w2New[1]:
            print("Xrange ", xRange, w2New)
            print("Yrange ", yRange, w2New)
            print("")


f = open("Day03/testinput.txt", "r")
w1 = f.readline()
w1_arr = w1.split(",")
w1_pos= [0,0]

w2 = f.readline()
w2_arr = w2.split(",")

for Wire1 in range( len(w1_arr) ):

    w1_oldpos = w1_pos[:] # Prevents referencing w1_pos
    w1_pos = wireMovement( w1_pos, w1_arr[Wire1])

    w2_pos = [0,0]
    for Wire2 in range( len(w2_arr) ):
        w2_oldpos = w2_pos[:]
        w2_pos = wireMovement( w2_pos, w2_arr[Wire2])
        CheckIntersection( w1_oldpos, w1_pos, w2_oldpos, w2_pos)
        
print("End Points : ", w1_oldpos, w2_oldpos)


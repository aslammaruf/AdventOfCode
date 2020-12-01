import math

f = open("Day02/input.txt", "r")
IntCode_Str = f.readline()
IntCode_Arr = IntCode_Str.split(",")

x = 0
opCode = 0

while int(opCode) != 99:
    opCode = int(IntCode_Arr[x])
    if opCode == 1:
        FirstNum = int(IntCode_Arr[x + 1])
        SecondNum = int(IntCode_Arr[x + 2])
        OutputPos = int(IntCode_Arr[x + 3])
        IntCode_Arr[OutputPos] = int(IntCode_Arr[FirstNum]) + int(IntCode_Arr[SecondNum])
    elif opCode == 2:
        FirstNum = int(IntCode_Arr[x + 1])
        SecondNum = int(IntCode_Arr[x + 2])
        OutputPos = int(IntCode_Arr[x + 3])
        IntCode_Arr[OutputPos] = int(IntCode_Arr[FirstNum]) * int(IntCode_Arr[SecondNum])

    x += 4 # Stepping Forward 4 Steps
    
print("Result in pos 0 : ", IntCode_Arr[0] )
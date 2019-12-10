import math

f = open("Day02/input.txt", "r")
IntCode_Str = f.readline()
IntCode_Arr = IntCode_Str.split(",")
Array_len = int(len(IntCode_Arr))

for pos1 in range(Array_len):
    for pos2 in range(Array_len):
        # Reset Array
        IntCode_Arr = IntCode_Str.split(",")
        opCode = 0
        x = 0
        # Change Values in pos 1 & 2
        IntCode_Arr[1] = str(pos1)
        IntCode_Arr[2] = str(pos2)
        # Run IntCode System
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
        # Check Result
        if IntCode_Arr[0] == 19690720:
            print( "Found : ", IntCode_Arr[0] )
            print( "Noun : ", pos1 )
            print( "Verb : ", pos2 )
            result = 100 * int(pos1) + int(pos2)
            print( "Final Result : ", result)
            exit()
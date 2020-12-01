f = open("Day05/input.txt", "r")
IntCode_Arr = f.readline().split(",")

x, opCode = (0, 0)
Input_ID = input("Enter Input Value : ")

def split_Opcode(num):
    op = abs(num) % 100
    c = (num // ( 10**2 )) % 10
    b = (num // ( 10**3 )) % 10
    a = (num // ( 10**4 )) % 10
    return op, c, b, a

def get_value(para, pos):
    if para == 0:
        return int( IntCode_Arr[ int(IntCode_Arr[pos])] )
    else:
        return int( IntCode_Arr[pos])

while int(opCode) != 99 or x == len(IntCode_Arr):
    opCode, c, b, a = split_Opcode( int(IntCode_Arr[x]) )
    if opCode == 1:
        IntCode_Arr[ int(IntCode_Arr[x + 3])] = get_value(c, x+1) + get_value(b, x+2)
        x += 4
    elif opCode == 2:
        IntCode_Arr[ int(IntCode_Arr[x + 3])] = get_value(c, x+1) * get_value(b, x+2)
        x += 4
    elif opCode == 3:
        IntCode_Arr[ int(IntCode_Arr[x + 1]) ] = Input_ID
        x += 2
    elif opCode == 4:
        print( get_value(c, x+1) )
        x += 2
    elif opCode == 5:
        if get_value(c, x+1) != 0:
            x = get_value(b, x+2)
        else:
            x += 3
    elif opCode == 6:
        if get_value(c, x+1) == 0:
            x = get_value(b, x+2)
        else:
            x += 3
    elif opCode == 7:
        if get_value(c, x+1) < get_value(b, x+2):
            IntCode_Arr[ int(IntCode_Arr[x + 3]) ] = 1
        else:
            IntCode_Arr[ int(IntCode_Arr[x + 3]) ] = 0
        x += 4
    elif opCode == 8:
        if get_value(c, x+1) == get_value(b, x+2):
            IntCode_Arr[ int(IntCode_Arr[x + 3]) ] = 1
        else:
            IntCode_Arr[ int(IntCode_Arr[x + 3]) ] = 0
        x += 4
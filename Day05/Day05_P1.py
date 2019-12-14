"""
    a b c 
    if 1 then use value in position
    if 0 then use number as location

    Opcode Split example if input is 1002
    a = 0, b = 1, c = 0 , op = 02
    number divided by 10^n mod 10
"""

f = open("Day05/input.txt", "r")
IntCode_Arr = f.readline().split(",")

x, opCode = (0, 0)
# Input_ID = input("Enter Input Id: ")
Input_ID = 1

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

while int(opCode) != 99:
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
        print( IntCode_Arr[ int(IntCode_Arr[x + 1]) ] )
        x += 2

def HandheldHalting():
    # Set local variable : i is Index, looped is a 0,1 bool, accumulator is the result, closedlist stores arr index that have been run
    i = looped = accumulator = 0
    closedList = []

    # Add current instruction to closedList, then run the instruction afterwards check if new i has been run already
    while not looped:
        closedList.append(i)
        
        i , accumulator = runInstruction( i , accumulator )

        if i in closedList:
            looped = 1

    return accumulator

def HandheldHaltingP2():
    # Set local variable : i is Index, looped is a 0,1 bool, accumulator is the result, closedlist stores arr index that have been run
    # changeList contains all 'nop' and 'jmp' index location
    # change the first nop or jmp

    i = x = accumulator = 0
    closedList = []
    changeList = [ i for i, instruction in enumerate( arr ) if instruction[0] == "nop" or instruction[0] == "jmp"]
    arr[ changeList[x] ][0] = "nop" if arr[ changeList[x] ][0] == "jmp" else "jmp"

    while i < len( arr ):
        closedList.append(i)

        i , accumulator = runInstruction( i , accumulator )

        if i in closedList:
            # Code runs when a repeated command is found
            # Change the variables to test the next iteration, and reset variables
            arr[ changeList[x] ][0] = "nop" if arr[ changeList[x] ][0] == "jmp" else "jmp"
            arr[ changeList[x + 1] ][0] = "nop" if arr[ changeList[x + 1] ][0] == "jmp" else "jmp"
            x += 1
            closedList = []
            i = accumulator = 0

    return accumulator

def runInstruction( i , accumulator ):
    if arr[i][0] == "nop":
        i += 1
    elif arr[i][0] == "acc":
        accumulator += int( arr[i][1] )
        i += 1
    elif arr[i][0] == "jmp":
        i += int( arr[i][1] )

    return i , accumulator

# Main

filename = "Day08/input.txt"
arr = [ line.split() for line in open( filename ).read().split('\n')]

print( f'Part 1 answer : {HandheldHalting()}')
print( f'Part 2 answer : {HandheldHaltingP2()}')
# https://docs.python.org/2/library/string.html#format-specification-mini-language
# format 036b : {0} Leading Zeros {36} fill till string is 36 len {b} converts to binary
from itertools import product

def DockingData():
    mask = []
    mem = {}

    for key, value in arr:
        if key == "mask":
            mask = list(value)
        else:
            # Convert value in to binary with leading zeros, Replace the "X" with 1 or 0
            # Add masked binary value to diction with key
            binValue = format( int(value), '036b' )
            masked = [ binValue[i] if char == "X" else char for i, char in enumerate(mask) ]
            mem[ key[4:-1] ] = "".join( masked )

    return sum([ int( value, 2 ) for value in mem.values() ])

def DockingDataP2():
    mask = []
    mem = {}

    for key, value in arr:
        if key == "mask":
            mask = list(value)
        else:
            # Convert Key into Binary, then apply Mask
            binKey = format( int(key[4:-1]), '036b' )
            masked = [ binKey[i] if char == "0" else char for i, char in enumerate(mask) ]
            # Create list of possible combinations based on number of X in masked
            x = [ seq for seq in product("01", repeat = masked.count("X")) ]
            # Creates list of indexs of where "X" in masked
            XIndex = [ i for i , x in enumerate(masked) if x == "X" ]

            for perm in x:
                
                for permIndex , i in enumerate(XIndex):
                    masked[i] = str(perm[permIndex])

                mem[ int( "".join(masked) , 2 ) ] = int(value)

    return sum( mem.values() )

# Main

filename = "Day14/input.txt"
arr = [ line.split(" = ") for line in open( filename ).read().split("\n")]

print( f'Part 1 answer : {DockingData()}')
print( f'Part 2 answer : {DockingDataP2()}')

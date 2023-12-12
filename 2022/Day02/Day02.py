# Part 1

def FunctionName( data ):
    total = 0

    for i in data:
        roundTotal = 0

        if ( ( i[0] == "A" and i[1] == "Y" ) or ( i[0] == "B" and i[1] == "Z" ) or ( i[0] == "C" and i[1] == "X" ) ):
            roundTotal += 6
        elif ( ( i[0] == "A" and i[1] == "Z" ) or ( i[0] == "B" and i[1] == "X" ) or ( i[0] == "C" and i[1] == "Y" ) ):
            roundTotal += 0
        else:
            roundTotal += 3

        if ( i[1] == "X" ):
            roundTotal += 1
        elif ( i[1] == "Y" ):
            roundTotal += 2
        elif ( i[1] == "Z" ):
            roundTotal += 3
        
        total += roundTotal

    return total

# Part 2

def FunctionName2( data ):
    total = 0

    for i in data:
        roundTotal = 0

        if i[1] == "X":
            if( i[0] == "A" ):
                roundTotal += 3
            elif( i[0] == "B" ):
                roundTotal += 1
            elif( i[0] == "C" ):
                roundTotal += 2
        elif i[1] == "Y":
            if( i[0] == "A" ):
                roundTotal += 1
            elif( i[0] == "B" ):
                roundTotal += 2
            elif( i[0] == "C" ):
                roundTotal += 3
            roundTotal += 3
        elif i[1] == "Z":
            if( i[0] == "A" ):
                roundTotal += 2
            elif( i[0] == "B" ):
                roundTotal += 3
            elif( i[0] == "C" ):
                roundTotal += 1
            roundTotal += 6
        
        total += roundTotal

    return total


with open('Day02/input.txt') as f:
    data = [ line.strip().split(" ") for line in f]

p1Answer = FunctionName( data )
p2Answer = FunctionName2( data )

print()
print(f'Part 1: : {p1Answer}')
print(f'Part 2: : {p2Answer}')
print()
# Part 1
calTotals = []

def FunctionName( data ):
    total = 0

    for i in range( 0, len(data)):
        if data[i] == "":
            calTotals.append(total)
            total = 0
        else:
            total = total + int(data[i])

    calTotals.append(total)
    return sorted(calTotals, reverse=True)[0]

# Part 2

def FunctionName2( data ):
    return sum( sorted(calTotals, reverse=True)[0:3] ) 


with open('Day01/input.txt') as f:
    data = [ line.strip() for line in f]

p1Answer = FunctionName( data )
p2Answer = FunctionName2( data )

print()
print(f'Part 1: : {p1Answer}')
print(f'Part 2: : {p2Answer}')
print()
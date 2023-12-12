# Part 1

def FunctionName( data ):

    return 0

# Part 2

def FunctionName2( data ):

    return 0


with open('Day12/test.txt') as f:
    data = [ int(line) for line in f]

p1Answer = FunctionName( data )
p2Answer = FunctionName2( data )

print()
print(f'Part 1: : {p1Answer}')
print(f'Part 2: : {p2Answer}')
print()
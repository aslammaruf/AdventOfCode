import os, re

# Part 1

def FunctionName( data ):

    return 0

# Part 2

def FunctionName2( data ):

    return 0


with open(f'{os.path.splitext(os.path.basename(__file__))[0]}-input.txt') as f:
    data = [ line for line in f]

p1Answer = FunctionName( data )
p2Answer = FunctionName2( data )

print()
print(f'Part 1: : {p1Answer}')
print(f'Part 2: : {p2Answer}')
print()
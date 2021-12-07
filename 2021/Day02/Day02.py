# Part 1

def Dive( arr ):
    forward = sum([ int(val[1]) if val[0] == 'forward' else 0 for val in arr])
    depth = sum([ int(val[1]) if val[0] == 'up' else -int(val[1]) if val[0] == 'down' else 0 for val in arr])
    return forward * abs( depth )

# Part 2

def Dive2( arr):
    aim, forward, depth = 0,0,0

    for com, x in arr:
        if com == 'down':
            aim += int(x)
        elif com == 'up':
            aim -= int(x)
        elif com == 'forward':
            forward += int(x)
            depth += aim * int(x)

    return forward * abs( depth )


with open('Day02/input.txt') as f:
    arr = [ line.split() for line in f]

p1Answer = Dive( arr )
p2Answer = Dive2( arr )

print()
print(f'Part 1: {p1Answer}')
print(f'Part 2: {p2Answer}')
print()

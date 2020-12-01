input = 265149

x, counter = 1, 1

# get the lowest and highest of the spiral, 1 - 9 - 25
while counter < input:
    temp = counter
    x += 1
    counter = (2 * x - 1) ** 2

# get distance from center
xcoord = (x - 1) / 2
mod = (input - temp) % ( xcoord * 2)
distance = xcoord + (mod - xcoord)
print( distance )



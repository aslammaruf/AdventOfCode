import math

fuel_req = 0

with open("Day01/input.txt") as f:
    for line in f:
        fuel_req += ( math.floor( int(line) / 3 ) - 2 )

print(fuel_req)
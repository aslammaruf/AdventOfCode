
def Lanternfish( data , days ):
    # fish[ day ] = [ number ]
    fish = [0] * 9
    for idx in range(0, 9):
        fish[idx] = data.count(idx)

    for _ in range(0, days):
        temp = fish[0]
        fish.pop(0)
        fish.append(temp)
        fish[6] += temp

    return sum(fish)

with open('Day06/input.txt') as f:
    data = list(map(int, [ line.split(',') for line in f ][0] ))

p1Answer = Lanternfish( data , 80 )
p2Answer = Lanternfish( data , 256 )

print()
print(f'Part 1: Number of fish after 80 days: {p1Answer}')
print(f'Part 2: Number of fish after 256 days: {p2Answer}')
print()

"""
# Part 1

def Lanternfish( data , days ):

    for day in range(1, days + 1):
        data = [ age - 1 for age in data ]
        data += [ 8 ] * data.count(-1)
        data = [ 6 if age < 0 else age for age in data ]
        # Debug Print
        #print( f'After {str(day).zfill(2)} days : {data}')

    return len(data)

"""
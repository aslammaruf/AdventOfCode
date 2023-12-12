# Part 1

def FunctionName( data ):
    total = 0

    for backpack in data:
        comp_1, comp_2 = set(list(backpack[0:int(len(backpack)/2)])), set(list(backpack[ int(len(backpack)/2):]))
        intersect = list(comp_1 & comp_2)[0]
        total += ord( intersect[0] ) - 96
        if intersect.isupper() : total += 58
        
    return total

# Part 2

def FunctionName2( data ):
    total = 0

    for i in range(0, len(data), 3):
        badge = list( set(list(data[i])) & set(list(data[i + 1])) & set(list(data[i + 2 ])) )[0]
        total += ord( badge ) - 96
        if badge.isupper() : total += 58

    return total


with open('Day03/input.txt') as f:
    data = [ line.strip() for line in f]

p1Answer = FunctionName( data )
p2Answer = FunctionName2( data )

print()
print(f'Part 1: : {p1Answer}')
print(f'Part 2: : {p2Answer}')
print()
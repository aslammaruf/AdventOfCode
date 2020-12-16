numDict = {
    0 : 1,
    20: 2,
    7 : 3,
    16: 4,
    1 : 5,
    18: 6,
}

i = len( numDict ) + 1
lns = 15 # Last Number Spoken - lns

while i < 30000000:
    if lns in numDict.keys():
        temp = lns
        lns = i - numDict[lns]
        numDict[temp] = i
    else:
        numDict[lns] = i
        lns = 0

    i += 1

    if i == 2020:
        print( f'Part 1 answer : {lns}')

print( f'Part 2 answer : {lns}' )

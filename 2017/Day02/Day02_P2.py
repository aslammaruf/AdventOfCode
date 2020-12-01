def CorruptionChecksum( line ):
    arr = line.split()
    arr.sort(key=int) 

    for x in arr:
        for y in arr:
            if int(x) % int(y) == 0 and x != y:
                rowChecksum = int(x) / int(y)

    print( rowChecksum)
    return rowChecksum
    

result = 0

with open("Day2_input.txt") as f:
    for line in f:
        result += CorruptionChecksum( line )

print(f"result = {result}")
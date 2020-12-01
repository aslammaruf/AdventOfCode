def CorruptionChecksum( line ):
    arr = line.split()
    arr.sort(key=int) 

    rowChecksum = int(arr[-1]) - int(arr[0])

    print( max((arr) )
    return int(rowChecksum)
    

result = 0

with open("Day2_input.txt") as f:
    for line in f:
        result += CorruptionChecksum( line )

print(f"result = {result}")
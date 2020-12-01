def memReallocation( arr ):
    cycles = [arr[:]]

    found = False
    while found == False:

        pos = arr.index(max(arr)) # gets the first position of the highest number in array
        value = arr[pos]
        arr[pos] = 0

        while value != 0:
            pos = pos + 1 if pos < len(arr) - 1 else 0
            arr[pos] += 1
            value -= 1
        
        found = arr in cycles
        cycles.append(arr[:])

    return len(cycles) - 1 - cycles.index(arr)
    
with open("Day6_input.txt") as f:
    for line in f:
        arr = list(map(int, line.split()))

    print(f'Inital Arr : {arr}')
    result = memReallocation( arr )

print(result)
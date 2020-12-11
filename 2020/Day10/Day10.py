import math

def AdapterArray():
    arr.sort()
    print( f'sorted arr : {arr}' )
    
    arrDiff = [ arr[i + 1] - value for i, value in enumerate(arr[:-1]) ] 

    print( f'arrDiff arr : {arrDiff}' )
    print( f'number of 1-jolt : {arrDiff.count(1) + 1}, number of 3-jolt : {arrDiff.count(3) + 1}' )
    return (arrDiff.count(1) + 1 ) * (arrDiff.count(3) + 1)

def AdapterArrayP2():
    return 0
    
# Main

filename = "Day10/test2.txt"
arr = [ int(line) for line in open( filename ).read().split("\n") ]

print( f'Part 1 answer : {AdapterArray()}')
print( f'Part 2 answer : {AdapterArrayP2()}')
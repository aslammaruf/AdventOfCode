import numpy as np

with open("2020/Day01/input.txt") as f:
    # Create Numpy Array of numbers from input file
    arr = np.array( [int(line) for line in f] )

filename = '2020/Day01/input.txt'
arr2 = np.array( [ int(x) for x in open(filename).read().split('\n')] )

print( arr )
print( arr2 )
import numpy as np

with open("Day01/input.txt") as f:
    print( sum( np.floor( np.array( [ int(line) / 3 - 2 for line in f] )) ) )
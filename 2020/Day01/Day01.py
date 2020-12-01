import numpy as np
from itertools import combinations

def ReportRepair( arr ):
    a, b = [np.where(arr == i) for i in ( 2020 - arr ) if i in arr]
    return *arr[a], *arr[b]

def ReportRepairP2( arr ):
    comb = list(combinations( arr, 3))
    combsum = np.sum(np.array(comb), 1)
    y =  int(*np.where(combsum == 2020))
    return comb[y]


with open("Day01/input.txt") as f:
    arr = np.array( [int(line) for line in f] )

a,b = ReportRepair( arr )

print(f'Part 1: 2 Entries that sum to 2020 are {a} and {b}')
print(f'Part 1: Product of the 2 entries are \n {a * b}')

a, b, c = ReportRepairP2( arr )


print(f'Part 2: 3 Entries that sum to 2020 are {a} , {b} and {c}')
print(f'Part 2: Product of the 2 entries are \n {a * b * c}')
# Part 1

def SonarSweep( arr ):
    count = 0
    for i in range(1, len(arr) ):
        if arr[i] > arr [i-1]:
            count += 1
    return count

def SonarSweepBS( arr ):
    output = [ True if arr[i] > arr[i-1] else False for i in range(1, len(arr)) ]
    return sum(output)

# Part 2

def SonarSweepP2( arr):
    count = 0
    for i in range(2, len(arr)):
        if arr[i]+arr[i-1]+arr[i-2] > arr [i-1]+arr[i-2]+arr[i-3]:
            count += 1
    return count


with open('Day01/input.txt') as f:
    arr = [ int(line) for line in f]

p1Answer = SonarSweepBS( arr )
p2Answer = SonarSweepP2( arr )

print()
print(f'Part 1: Number of measurements larger than previous : {p1Answer}')
print(f'Part 2: 3 Measurement Sliding Window : {p2Answer}')
print()

# 1676
# 1706
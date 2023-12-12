import os, re

# Part 1

def FunctionName( data ):
    ans = []
    for calibration in data:
        m = re.findall( '\d', calibration )
        ans.append( int(m[0] + m[-1] ))

    return sum(ans)

# Part 2

def FunctionName2( data ):
    ans2 = []
    numdict = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for calibration in data:
        m = re.findall( r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', calibration )
        print( m )
        for index, num in enumerate(m):
            try: 
                int(num)
            except:
                m[index] = numdict.index(num)
        ans2.append( int(str(m[0]) + str(m[-1]) ))
    print( ans2 )
    return sum(ans2)


with open(f'{os.path.splitext(os.path.basename(__file__))[0]}-input.txt') as f:
    data = [ line.strip() for line in f]

#p1Answer = FunctionName( data )
p2Answer = FunctionName2( data )

print()
#print(f'Part 1: : {p1Answer}')
print(f'Part 2: : {p2Answer}')
print()
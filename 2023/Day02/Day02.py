import os, re

# Part 1

def FunctionName( data ):
    red = 12
    green = 13
    blue = 14
    ans = []
    for game in data:
        m = re.findall( r'[0-9]{1,2}(?= red)' , game)
        m = [ int(num) for num in m if int(num)>red ]
        if len(m)>0:
            continue
        m = re.findall( r'[0-9]{1,2}(?= green)' , game)
        m = [ int(num) for num in m if int(num)>green ]
        if len(m)>0:
            continue
        m = re.findall( r'[0-9]{1,2}(?= blue)' , game)
        m = [ int(num) for num in m if int(num)>blue ]
        if len(m)>0:
            continue
        ans.append( int(re.search(r'(?<=Game )[0-9]+', game).group(0)) )
    return sum( ans )

# Part 2

def FunctionName2( data ):
    ans = []
    for game in data:
        print( game )
        r = list(map(int, re.findall( r'[0-9]{1,2}(?= red)' , game)))
        r.sort()
        g = list(map(int, re.findall( r'[0-9]{1,2}(?= green)' , game)))
        g.sort()
        b = list(map(int, re.findall( r'[0-9]{1,2}(?= blue)' , game)))
        b.sort()

        ans.append( r[-1] * g[-1] * b[-1])
    return sum( ans )


with open(f'{os.path.splitext(os.path.basename(__file__))[0]}-input.txt') as f:
    data = [ line.strip() for line in f]

p1Answer = FunctionName( data )
p2Answer = FunctionName2( data )

print()
print(f'Part 1: : {p1Answer}')
print(f'Part 2: : {p2Answer}')
print()
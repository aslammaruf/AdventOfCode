import os, re

# Part 1
def checksymbol( string ):
    filtered = re.sub( r'\d|\.', '', string)
    return False if filtered == "" else True

def FunctionName( data ):
    ans = []
    
    for index, row in enumerate(data):
        m = re.finditer(r'[0-9]+', row)
        for match in m:
            num = match.group(0)
            numrange = match.span()

            string = ""
            for coordrow in range( numrange[0] - 1, numrange[1] + 1):
                if coordrow >= 0 and coordrow <= len(row)-1: 
                    a = data[index - 1][coordrow] if index > 0 else "."
                    b = data[index][coordrow]
                    c = data[index + 1][coordrow] if index < len(data)-1 else "."
                    string += a + b + c
            if checksymbol( string ): 
                ans.append( int(num) )

    return sum(ans)


# Part 2
def getnum(data, index, coordrow, char, increment, forward = False):
    x = ""
    i = 0
    while char.isalnum():
        if coordrow + i >= 0 and coordrow + i <= len(data[0])-1: 
            char = data[index][ coordrow + i ]
            x =  x + char if forward else char + x
            i += increment
        else: char = "."
    return x

def FunctionName2( data ):
    ans = []
    
    for index, row in enumerate(data):
        m = re.finditer(r'\*', row)
        for match in m:
            num = match.group(0)
            numrange = match.span()

            rows = [ "", "", ""]
            for coordrow in range( numrange[0] - 1, numrange[1] + 1):
                if coordrow >= 0 and coordrow <= len(row)-1: 
                    a = data[index - 1][coordrow] if index > 0 else "."
                    b = data[index][coordrow]
                    c = data[index + 1][coordrow] if index < len(data)-1 else "."
                    if coordrow == numrange[0] - 1:
                        a = getnum(data, index - 1, coordrow, a, -1)
                        b = getnum(data, index, coordrow, b, -1)
                        c = getnum(data, index + 1, coordrow, c, -1)
                    if coordrow == numrange[1]:
                        a = getnum(data, index - 1, coordrow, a, 1, True)
                        b = getnum(data, index, coordrow, b, 1, True)
                        c = getnum(data, index + 1, coordrow, c, 1, True)
                    rows[0] += a
                    rows[1] += b
                    rows[2] += c
            x = ''
            y  = re.sub( r'\.|\*', ' ',  x.join(rows))
            y = y.split()
            if len(y) == 2:
                ans.append( int(y[0]) * int(y[1]) )
    return sum(ans)


with open(f'{os.path.splitext(os.path.basename(__file__))[0]}-input.txt') as f:
    data = [ line.strip() for line in f]

p1Answer = FunctionName( data )
p2Answer = FunctionName2( data )

print()
print(f'Part 1: : {p1Answer}')
print(f'Part 2: : {p2Answer}')
print()